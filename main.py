# import tkinter as tk
import classes
from setup import *
import pickle
from PIL import ImageTk, Image
import os.path
from os import path


def save_devices():
    # Can't pickle tKinter objects. Need to convert xpos, ypos, and image to dict
    devices_to_pickle = []
    for d in all_devices:
        this_device = {'image_path': d.__dict__['image_path'],
                       'xpos': d.__dict__['xpos'],
                       'ypos': d.__dict__['ypos']}
        # devices_to_pickle.append(d.__dict__)
        devices_to_pickle.append(this_device)
    print(devices_to_pickle)
    pickle_out = open("saved_locations\devices.pk1", "wb")
    pickle.dump(devices_to_pickle, pickle_out)
    pickle_out.close()
    print("SAVED DEVICES!!!!")


def add_device():
    print("New device code to add")


save_button = tk.Button(program_canvas.root, text="Save", command=save_devices)
save_button.pack(pady=20)
new_device_button = classes.NewDeviceButton(program_canvas.canvas)
classes.DeleteDeviceButton(program_canvas.canvas)


if path.exists("saved_locations/devices.pk1"):
    classes.FloorPlan(program_canvas.canvas, "apartment.png")
else:
    classes.FloorPlan(program_canvas.canvas, "apartment.png")


if path.exists("saved_locations/devices.pk1"):
    pickle_in = open("saved_locations/devices.pk1", "rb")
    saved_devices = pickle.load(pickle_in)
    for d in saved_devices:
        all_devices.append(classes.DeviceIcon(program_canvas.canvas,
                                              d['image_path'].split("/")[-1:][0],
                                              d['xpos'],
                                              d['ypos']))
else:
    program_canvas.alert_message.config(text="No devices on this floorplan")
    # ypos = 150
    # while ypos < 400:
    #     all_devices.append(widgets.DeviceIcon(program_canvas.canvas, "green_circle.png", 100, ypos))
    #     ypos += 100


program_canvas.root.mainloop()
