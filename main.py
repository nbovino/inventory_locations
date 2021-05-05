import tkinter as tk
import classes
from global_variables import *
# from setup import *
import pickle
from PIL import ImageTk, Image
import os.path
from os import path

# all_devices = []
#
# IMAGE_PATH = "images/"
# LAYOUTS_PATH = "layouts/"
# DEVICE_ICONS_PATH = "device_icons/"
#
# w = 600
# h = 400
# # Starting coordinates of the circle
# x = w // 2
# y = h // 2


class BaseWindow(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Inventory Locations')
        # root.iconbitmap("\\images\\greeen_circle.png")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, width=w, height=h, bg="white")
        # self.canvas.pack(pady=20)
        self.canvas.grid(row=1, rowspan=5, column=1, columnspan=8)
        # self.alert_message = tk.Label(self.root, text="HELLO")
        # Pack
        # self.alert_message.pack(pady=30, side=tk.RIGHT)
        # self.alert_message.grid(row=10, rowspan=1, column=1, columnspan=1)
        self.selected_device = None
        self.save_button = tk.Button(self.root, text="Save", command=save_devices)
        # self.save_button.pack(pady=20)
        self.save_button.grid(row=3, rowspan=1, column=10, columnspan=1)
        new_device_button = classes.NewDeviceButton(self.canvas, self.root, all_devices)
        # classes.DeleteDeviceButton(program_canvas.canvas)

        # Load floorplan
        if path.exists("saved_locations/devices.pk1"):
            classes.FloorPlan(self.canvas, "apartment.png")
        else:
            classes.FloorPlan(self.canvas, "apartment.png")

        # Load devices
        if path.exists("saved_locations/devices.pk1"):
            pickle_in = open("saved_locations/devices.pk1", "rb")
            saved_devices = pickle.load(pickle_in)
            for d in saved_devices:
                all_devices.append(classes.DeviceIcon(self.canvas,
                                                      d['image_path'].split("/")[-1:][0],
                                                      d['xpos'],
                                                      d['ypos'],
                                                      self.root,
                                                      d['device_name']))
        else:
            print("No Devices on the floorplan")
            # self.alert_message.config(text="No devices on this floorplan")


def save_devices():
    # Can't pickle tKinter objects. Need to convert xpos, ypos, and image to dict
    devices_to_pickle = []
    for d in all_devices:
        this_device = {'image_path': d.__dict__['image_path'],
                       'xpos': d.__dict__['xpos'],
                       'ypos': d.__dict__['ypos'],
                       'device_name': d.__dict__['device_name']}
        # devices_to_pickle.append(d.__dict__)
        devices_to_pickle.append(this_device)
    print(devices_to_pickle)
    pickle_out = open("saved_locations\devices.pk1", "wb")
    pickle.dump(devices_to_pickle, pickle_out)
    pickle_out.close()
    print("SAVED DEVICES!!!!")


def add_device():
    print("New device code to add")


program_setup = BaseWindow()

program_setup.root.mainloop()
