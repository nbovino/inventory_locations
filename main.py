import tkinter as tk
import classes
import global_variables
import json
# from setup import *
import pickle
from PIL import ImageTk, Image
import os


class BaseWindow(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Inventory Locations')
        # self.current_floor_plan = None
        # root.iconbitmap("\\images\\greeen_circle.png")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, width=global_variables.w, height=global_variables.h, bg="white")
        # self.canvas.pack(pady=20)
        self.canvas.grid(row=1, rowspan=10, column=1, columnspan=10)
        # self.alert_message = tk.Label(self.root, text="HELLO")
        # Pack
        # self.alert_message.pack(pady=30, side=tk.RIGHT)
        # self.alert_message.grid(row=10, rowspan=1, column=1, columnspan=1)
        self.save_button = tk.Button(self.root, text="Save", command=save_devices)
        # self.save_button.pack(pady=20)
        self.save_button.grid(row=5, rowspan=1, column=11, columnspan=1)
        new_device_button = classes.NewDeviceButton(self.canvas, self.root, global_variables.floor_plan_devices)
        move_devices_button = classes.MoveDevicesButton(self.canvas, self.root)
        self.delete_device_button = tk.Button(self.root, text="Delete Device",
                                              command=delete_device)
        self.delete_device_button.grid(row=4, rowspan=1, column=11, columnspan=1)
        # classes.DeleteDeviceButton(program_canvas.canvas)
        self.floor_plan_list = classes.FloorPlanList(self.root)
        # self.load_fp_button = tk.Button(self.root, text="Load Floor Plan", command=lambda: load_plan(self.floor_plan_list))
        # The lambda that this causes to happen sends the selected item in the listbox
        self.load_fp_button = tk.Button(self.root, text="Load Floor Plan",
                                        command=lambda: load_plan(root=self.root,
                                                                  canvas=self.canvas,
                                                                  floor_plan_name=self.floor_plan_list.floor_plan_listbox.get(self.floor_plan_list.floor_plan_listbox.curselection()[0])#,
                                                                  #loaded_devices=get_devices_of_floor_plan(self.floor_plan_list.floor_plan_listbox.get(self.floor_plan_list.floor_plan_listbox.curselection()[0])))
                                                                  )
                                        )
        self.load_fp_button.grid(row=11, rowspan=1, column=3, columnspan=1)

        # Load floorplan
        load_plan(floor_plan_name=None, root=self.root, canvas=self.canvas)
        self.floor_plan_list.add_all_floor_plans(sorted(global_variables.floor_plans))


# returns list of devices in floor plan
def get_devices_of_floor_plan(floor_plan):
    try:
        with open('saved_locations/floor_plan_data.json') as f:
            json_data = json.load(f)
            print("json Data!!!!!!!!!!!!!!")
            print(json_data[floor_plan])
            devices_to_return = []
            for d in json_data[floor_plan]:
                devices_to_return.append(classes.DeviceIcon(program_setup.canvas,
                                                            d['image_path'].split("/")[-1:][0],
                                                            d['xpos'],
                                                            d['ypos'],
                                                            program_setup.root,
                                                            d['device_name']))
            # return json_data[floor_plan]
            return devices_to_return
    except:
        return None


# Loads devices to floor plan
def load_devices_to_floor_plan(devices):
    print("LOAD DEVICES TO FLOOR PLAN and current FP is: " + global_variables.current_floor_plan)
    # Reset the floor_plan_devices to zero
    global_variables.floor_plan_devices = []
    print(type(devices))
    # TODO: This is not working because when reading from saved data it is a list of dictionaries of the different
    # when loading, devices is a list of dicts read from json data,
    # but when deleting it is reading a list of DeviceIcon objects already loaded
    # so when a device is deleted, it displays the floor plan but program stops before it loads the devices b/c they are objects
    for d in devices:
        print(type(d))
        # TODO: This is not the way to do this. I should always pass the same kind of data to the function.
        # try:
        #     global_variables.floor_plan_devices.append(classes.DeviceIcon(program_setup.canvas,
        #                                                                   d['image_path'].split("/")[-1:][0],
        #                                                                   d['xpos'],
        #                                                                   d['ypos'],
        #                                                                   program_setup.root,
        #                                                                   d['device_name']))
        # except TypeError:
        global_variables.floor_plan_devices.append(classes.DeviceIcon(program_setup.canvas,
                                                                      d.__dict__['image_path'].split("/")[-1:][0],
                                                                      d.__dict__['xpos'],
                                                                      d.__dict__['ypos'],
                                                                      program_setup.root,
                                                                      d.__dict__['device_name']))


def load_plan(root, canvas, floor_plan_name=None, loaded_devices=None):
    print(floor_plan_name)
    print("Loaded devices on this floor plan:")
    print(loaded_devices)
    # TODO: If global_variables.made_changes is True, ask the user to verify they really want to load another floor plan
    # TODO: since the changes will not be saved if they load another floor plan if it was not saved.

    # If there is a floor plan name, load the floor plan
    if floor_plan_name:
        if os.path.exists("saved_locations/devices.pk1"):
            global_variables.current_floor_plan = floor_plan_name
            print("Current floor plan is: ")
            print(global_variables.current_floor_plan)
            # Display floor plan
            classes.FloorPlan(canvas, floor_plan_name + ".png")
        # If there are loaded devices, load the devices
        if loaded_devices and len(loaded_devices) > 0:
            print("THERE ARE DEVICES ON THIS FLOOR PLAN")
            # print(type(loaded_devices))
            load_devices_to_floor_plan(loaded_devices)
        # else, say there are no devices in the floor plan
        else:
            # check to see if there are any devices saved for the floor plan and try that
            load_devices_to_floor_plan(get_devices_of_floor_plan(global_variables.current_floor_plan))
    # else - no floor plan selected
    else:
        print("No floor plan selected")


def confirm_delete_device(confirm_window):
    print("Delete Device")
    # program_setup.canvas.delete(global_variables.selected_device)
    # The device is being deleted from the current floor plan devices list
    print(global_variables.floor_plan_devices)
    global_variables.floor_plan_devices.remove(global_variables.selected_device)
    print("AFTER DELETING THE DEVICE")
    print(global_variables.floor_plan_devices)
    # load_devices_to_floor_plan(global_variables.floor_plan_devices)
    confirm_window.destroy()
    global_variables.selected_device = None
    global_variables.made_changes = True
    load_plan(root=program_setup.root,
              canvas=program_setup.canvas,
              floor_plan_name=global_variables.current_floor_plan,
              loaded_devices=global_variables.floor_plan_devices)


def cancel_delete_device(confirm_window):
    confirm_window.destroy()
    global_variables.selected_device = None


def delete_device():
    if global_variables.selected_device:
        print(global_variables.selected_device.device_name)
        confirm_delete_window = tk.Toplevel(width=100, height=100)
        confirm_delete_window.geometry("%dx%d%+d%+d" % (200, 100, 250, 125))
        confirm_delete_window.title("Really!?")
        confirm_message = tk.Label(master=confirm_delete_window, text="Do you want to delete this device?\nThis cannot be undone")
        confirm_message.pack()
        device_info = tk.Label(master=confirm_delete_window, text=global_variables.selected_device.device_name)
        device_info.pack()
        # device_name.grid(row=0, column=0, columnspan=2)
        confirm = tk.Button(master=confirm_delete_window, text="Yes, Delete",
                            command=lambda: confirm_delete_device(confirm_delete_window))
        confirm.pack()
        cancel_button = tk.Button(master=confirm_delete_window, text="Cancel",
                                  command=lambda: cancel_delete_device(confirm_delete_window))
        # cancel_button.grid(row=1, column=1, columnspan=1)
        cancel_button.pack()


def save_devices():
    # Can't pickle tKinter objects. Need to convert xpos, ypos, and image to dict
    devices_to_save_in_floor_plan = []
    # for d in global_variables.floor_plan_devices:
    #     this_device = {'device_name': d.__dict__['device_name'],
    #                    'image_path': d.__dict__['image_path'],
    #                    'xpos': d.__dict__['xpos'],
    #                    'ypos': d.__dict__['ypos'],
    #                    'floor_plan': global_variables.current_floor_plan}
    #     # devices_to_save_in_floor_plan.append(d.__dict__)
    #     devices_to_save_in_floor_plan.append(this_device)
    # print(devices_to_save_in_floor_plan)
    # pickle_out = open("saved_locations\devices.pk1", "wb")
    # pickle.dump(devices_to_save_in_floor_plan, pickle_out)
    # pickle_out.close()
    # print("SAVED DEVICES!!!!")

    # json_save_data = {program_setup.current_floor_plan: devices_to_save_in_floor_plan}
    # This will save it to a json file instead of pickling
    # Try to open a file with floor plans in it
    for d in global_variables.floor_plan_devices:
        devices_to_save_in_floor_plan.append({'device_name': d.__dict__['device_name'],
                                              'image_path': d.__dict__['image_path'],
                                              'xpos': d.__dict__['xpos'],
                                              'ypos': d.__dict__['ypos'],
                                              'floor_plan': global_variables.current_floor_plan})
    try:
        # TODO: If there is no file to open, then create a file
        with open('saved_locations/floor_plan_data.json') as f:
            loaded_devices = json.load(f)
        loaded_devices[global_variables.current_floor_plan] = devices_to_save_in_floor_plan
    # If there is no floor plan saved yet it will throw an error, then it should create a new line
    except json.decoder.JSONDecodeError:
        loaded_devices = {global_variables.current_floor_plan: devices_to_save_in_floor_plan}
    with open('saved_locations/floor_plan_data.json', 'w') as outfile:
        json.dump(loaded_devices, outfile, indent=4)
    global_variables.made_changes = False


def add_device():
    print("New device code to add")


program_setup = BaseWindow()

program_setup.root.mainloop()
