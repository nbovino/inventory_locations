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
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, width=global_variables.w, height=global_variables.h, bg="white")
        self.canvas.grid(row=1, rowspan=10, column=1, columnspan=10)
        self.save_button = tk.Button(self.root, text="Save", command=save_devices)
        self.save_button.grid(row=5, rowspan=1, column=11, columnspan=1)
        self.move_devices_label = tk.Label(self.root, text="")
        self.move_devices_label.grid(row=3, column=12)
        self.move_devices_button = classes.MoveDevicesButton(self.canvas, self.root, self.move_devices_label)
        self.delete_device_button = tk.Button(self.root, text="Delete Device",
                                              command=delete_device)
        self.delete_device_button.grid(row=4, rowspan=1, column=11, columnspan=1)
        self.floor_plan_list = classes.FloorPlanList(self.root)

        # The lambda that this causes to happen sends the selected item in the listbox
        self.load_fp_button = tk.Button(self.root, text="Load Floor Plan",
                                        command=lambda: load_new_plan(canvas=self.canvas,
                                                                      floor_plan_name=self.floor_plan_list.floor_plan_listbox.get(self.floor_plan_list.floor_plan_listbox.curselection()[0])
                                                                      )
                                        )
        self.load_fp_button.grid(row=11, rowspan=1, column=3, columnspan=1)
        self.add_new_fp_button = tk.Button(self.root, text="Add New Floor Plan", command=lambda: print("Add new floor plan"))
        self.add_new_fp_button.grid(row=12, rowspan=1, column=3, columnspan=1)

        # TODO: make this into it's own class. Then can possibly alter it when clicking a device
        self.data_label = tk.Label(self.root, text="No device selected")
        self.data_label.grid(row=11, rowspan=1, column=4, columnspan=1)
        self.new_device_button = classes.NewDeviceButton(self.canvas, self.root, global_variables.floor_plan_devices, self.data_label)

        self.floor_plan_list.add_all_floor_plans(sorted(global_variables.floor_plans))


def destroy_all():
    for widget in program_setup.root.winfo_children():
        if isinstance(widget, tk.Toplevel):
            widget.destroy()


def get_saved_json_data():
    with open('saved_locations/floor_plan_data.json') as f:
        return json.load(f)


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
                                                            d['device_name'],
                                                            program_setup.data_label))
            # return json_data[floor_plan]
            return devices_to_return
    except:
        return None


# Loads devices to floor plan and clears out old list if it is populated
def populate_floor_plan_device_list(json_data_list):
    global_variables.floor_plan_devices.clear()
    for d in json_data_list:
        global_variables.floor_plan_devices.append(classes.DeviceIcon(program_setup.canvas,
                                                                      d['image_path'].split("/")[-1:][0],
                                                                      d['xpos'],
                                                                      d['ypos'],
                                                                      program_setup.root,
                                                                      d['device_name'],
                                                                      program_setup.data_label))


def load_floor_plan_after_deleting_device():
    # Copy to new temporary variable
    temp_devices = global_variables.floor_plan_devices.copy()

    # Clear list of devices
    global_variables.floor_plan_devices.clear()

    # Repopulate devices
    for d in temp_devices:
        global_variables.floor_plan_devices.append(classes.DeviceIcon(program_setup.canvas,
                                                                      d.__dict__['image_path'].split("/")[-1:][0],
                                                                      d.__dict__['xpos'],
                                                                      d.__dict__['ypos'],
                                                                      program_setup.root,
                                                                      d.__dict__['device_name'],
                                                                      program_setup.device_data))
    del temp_devices


def close_extra_window(closing):
    closing.destroy()


def confirm_load_without_saving(close_window):
    close_window.destroy()
    global_variables.made_changes = False
    load_new_plan(canvas=program_setup.canvas,
                  floor_plan_name=program_setup.floor_plan_list.floor_plan_listbox.get(
                      program_setup.floor_plan_list.floor_plan_listbox.curselection()[0])
                  )


# confirmation window to make sure user wants to load a new plan before saving changes
def confirm_load_without_saving_window():
    confirm_load_window = tk.Toplevel(width=100, height=100)
    confirm_load_window.geometry("%dx%d%+d%+d" % (200, 100, 250, 125))
    confirm_message = tk.Label(master=confirm_load_window,
                               text="You have not saved yet.\nLoading a new plan will lose any unsaved changes")
    confirm_message.pack()
    confirm = tk.Button(master=confirm_load_window, text="Load without saving",
                        command=lambda: confirm_load_without_saving(confirm_load_window)
                        )
    confirm.pack()
    cancel_button = tk.Button(master=confirm_load_window, text="Cancel",
                              command=lambda: close_extra_window(confirm_load_window))
    # cancel_button.grid(row=1, column=1, columnspan=1)
    cancel_button.pack()


# This loads from saved json data. Only when a new floor plan is loaded
def load_new_plan(canvas, floor_plan_name=None):
    # Check if there have been changes made
    if not global_variables.made_changes:
        # If there is a floor plan name, load the floor plan
        if floor_plan_name:
            # Reassign current floor plan
            global_variables.current_floor_plan = floor_plan_name

            # Load image of floor plan to canvas
            classes.FloorPlan(canvas, floor_plan_name + ".png")

            # GET DATA FROM JSON FILE
            json_data = get_saved_json_data()

            # Populate the floor_plan_devices list with json data
            populate_floor_plan_device_list(json_data[global_variables.current_floor_plan])

            # Make sure the move toggle is off
            program_setup.move_devices_label.config(text="")
            global_variables.devices_movable = False
            global_variables.selected_device = None
            program_setup.data_label.config(text="No device selected")

            # Delete loaded json_data to save space
            del json_data

        # else - no floor plan selected
        else:
            print("No floor plan selected")
    else:
        # Confirm you want to load before saving current floor plan
        confirm_load_without_saving_window()


def confirm_delete_device(confirm_window):
    print("Delete Device")

    # Remove device from global variable list
    global_variables.floor_plan_devices.remove(global_variables.selected_device)
    confirm_window.destroy()

    # Unselect the device that will be deleted
    global_variables.selected_device = None

    # Set made_changes to it knows it will need to be saved
    global_variables.made_changes = True

    # Remove everything from the canvas
    program_setup.canvas.delete("all")

    # Reload the floor plan
    classes.FloorPlan(program_setup.canvas, global_variables.current_floor_plan + ".png")
    load_floor_plan_after_deleting_device()
    # load_devices_to_floor_plan(global_variables.floor_plan_devices)


def cancel_delete_device(confirm_window):
    confirm_window.destroy()
    global_variables.selected_device = None


# Creates a confirm delete device window
def delete_device():
    if global_variables.selected_device:
        print(global_variables.selected_device.device_name)
        confirm_delete_window = tk.Toplevel(width=100, height=100)
        confirm_delete_window.geometry("%dx%d%+d%+d" % (200, 200, 250, 125))
        confirm_delete_window.title("Are you sure?")
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
    print("SAVING")
    print(global_variables.floor_plan_devices)
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
    global_variables.devices_movable = False
    global_variables.selected_device = None
    program_setup.move_devices_label.config(text="")
    program_setup.data_label.config(text="No device selected")

#
# def add_device():
#     print("New device code to add")


program_setup = BaseWindow()
load_new_plan(floor_plan_name=None, canvas=program_setup.canvas)
program_setup.root.mainloop()
