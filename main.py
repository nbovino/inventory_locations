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
        self.current_floor_plan = None
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
                                        command=lambda: load_plan(fp_list=self.floor_plan_list.floor_plan_listbox.get(self.floor_plan_list.floor_plan_listbox.curselection()[0]),
                                                                  root=self.root,
                                                                  canvas=self.canvas))
        self.load_fp_button.grid(row=11, rowspan=1, column=3, columnspan=1)

        # Load floorplan
        load_plan(fp_list=None, root=self.root, canvas=self.canvas)
        self.floor_plan_list.add_all_floor_plans(sorted(global_variables.floor_plans))


# Loads devices to floor plan
def load_devices_to_floor_plan(devices):
    if program_setup.current_floor_plan in devices:
        # if d['floor_plan'] == program_setup.current_floor_plan:
        for d in devices[program_setup.current_floor_plan]:
            global_variables.floor_plan_devices.append(classes.DeviceIcon(program_setup.canvas,
                                                                          d['image_path'].split("/")[-1:][0],
                                                                          d['xpos'],
                                                                          d['ypos'],
                                                                          program_setup.root,
                                                                          d['device_name']))


def confirm_delete_device(confirm_window):
    print("Delete Device")
    # TODO: Delete the selected device by doing the following
    program_setup.canvas.delete(global_variables.selected_device)
    global_variables.floor_plan_devices.remove(global_variables.selected_device)
    # load_devices_to_floor_plan(global_variables.floor_plan_devices)
    load_plan(fp_list=program_setup.current_floor_plan,
              root=program_setup.root,
              canvas=program_setup.canvas,
              loaded_devices=global_variables.floor_plan_devices)
    # If the device floor plan is the same as the current floor plan, then delete it from the floor plan list
    # Might have to move the current floor plan to be in global_variable.py instead of an attribute of the BaseWindow
    confirm_window.destroy()
    global_variables.made_changes = True


def cancel_delete_device(confirm_window):
    confirm_window.destroy()
    global_variables.selected_device = None


def delete_device():
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
    devices_to_pickle = []
    for d in global_variables.floor_plan_devices:
        this_device = {'device_name': d.__dict__['device_name'],
                       'image_path': d.__dict__['image_path'],
                       'xpos': d.__dict__['xpos'],
                       'ypos': d.__dict__['ypos'],
                       'floor_plan': program_setup.current_floor_plan}
        # devices_to_pickle.append(d.__dict__)
        devices_to_pickle.append(this_device)
    print(devices_to_pickle)
    pickle_out = open("saved_locations\devices.pk1", "wb")
    pickle.dump(devices_to_pickle, pickle_out)
    pickle_out.close()
    print("SAVED DEVICES!!!!")

    # json_save_data = {program_setup.current_floor_plan: devices_to_pickle}
    # This will save it to a json file instead of pickling
    # Try to open a file with floor plans in it
    try:
        # TODO: If there is no file to open, then create a file
        with open('saved_locations/floor_plan_data.json') as f:
            loaded_devices = json.load(f)
        loaded_devices[program_setup.current_floor_plan] = devices_to_pickle
    # If there is no floor plan saved yet it will throw an error, then it should create a new line
    except json.decoder.JSONDecodeError:
        loaded_devices = {program_setup.current_floor_plan: devices_to_pickle}
    with open('saved_locations/floor_plan_data.json', 'w') as outfile:
        json.dump(loaded_devices, outfile, indent=4)
    global_variables.made_changes = False


def load_plan(fp_list, root, canvas, loaded_devices=None):
    print(fp_list)
    # TODO: If global_variables.made_changes is True, ask the user to verify they really want to load another floor plan
    # TODO: since the changes will not be saved if they load another floor plan if it was not saved.
    if loaded_devices is None:
        try:
            with open('saved_locations/floor_plan_data.json') as f:
                loaded_devices = json.load(f)
        except:
            loaded_devices = ""
        print(loaded_devices)

    if fp_list:
        if os.path.exists("saved_locations/devices.pk1"):
            classes.FloorPlan(canvas, fp_list + ".png")
            program_setup.current_floor_plan = fp_list
        else:
            classes.FloorPlan(canvas, fp_list + ".png")
            program_setup.current_floor_plan = fp_list

        if os.path.exists("saved_locations/devices.pk1"):
            pickle_in = open("saved_locations/devices.pk1", "rb")
            saved_devices = pickle.load(pickle_in)
            # Will have to destroy all devices currently showing before adding these.
            # for d in floor_plan_devices:
            #     d.destroy()
            #     print("destroyed")
            global_variables.floor_plan_devices.clear()
            # for d in saved_devices:
            try:
                load_devices_to_floor_plan(loaded_devices)
                # if program_setup.current_floor_plan in loaded_devices:
                #     # if d['floor_plan'] == program_setup.current_floor_plan:
                #     for d in loaded_devices[program_setup.current_floor_plan]:
                #         global_variables.floor_plan_devices.append(classes.DeviceIcon(canvas,
                #                                                                       d['image_path'].split("/")[-1:][0],
                #                                                                       d['xpos'],
                #                                                                       d['ypos'],
                #                                                                       root,
                #                                                                       d['device_name']))
            except:
                pass
        else:
            print("No Devices on the floorplan")


def add_device():
    print("New device code to add")


program_setup = BaseWindow()

program_setup.root.mainloop()
