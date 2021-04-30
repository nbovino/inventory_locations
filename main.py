# import tkinter as tk
import widgets
from setup import *
import pickle
from PIL import ImageTk, Image
import os.path
from os import path

canvas.pack(pady=20)


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


save_button = tk.Button(root, text="Save", command=save_devices)
save_button.pack(pady=20)
new_device_button = widgets.NewDeviceButton(canvas)
# B1-Motion is when button one is pressed on mouse
# canvas.bind("<B1-Motion>", move)
# canvas.bind("<Button 1>", new_icon)


if path.exists("saved_locations/devices.pk1"):
    widgets.FloorPlan(canvas, "apartment.png")


if path.exists("saved_locations/devices.pk1"):
    pickle_in = open("saved_locations/devices.pk1", "rb")
    saved_devices = pickle.load(pickle_in)
    for d in saved_devices:
        all_devices.append(widgets.DeviceIcon(canvas,
                                              d['image_path'].split("/")[-1:][0],
                                              d['xpos'],
                                              d['ypos']))
else:
    ypos = 150
    while ypos < 400:
        all_devices.append(widgets.DeviceIcon(canvas, "green_circle.png", 100, ypos))
        ypos += 100

root.mainloop()
