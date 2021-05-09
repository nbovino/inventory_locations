import tkinter as tk
from global_variables import *
# from setup import *
import classes_testing
import setup_testing
import pickle
from PIL import ImageTk, Image
import os.path
from os import path

all_devices = []
#
IMAGE_PATH = "images/"
LAYOUTS_PATH = "layouts/"
DEVICE_ICONS_PATH = "device_icons/"
#
w = 600
h = 400
# # Starting coordinates of the circle
x = w // 2
y = h // 2

root = tk.Tk()
root.title('Inventory Locations')
# root.iconbitmap("\\images\\greeen_circle.png")
root.geometry("800x600")
canvas = tk.Canvas(root, width=w, height=h, bg="white")
# self.canvas.pack(pady=20)
canvas.grid(row=1, rowspan=5, column=1, columnspan=8)
# self.alert_message = tk.Label(self.root, text="HELLO")
# Pack
# self.alert_message.pack(pady=30, side=tk.RIGHT)
# self.alert_message.grid(row=10, rowspan=1, column=1, columnspan=1)


def save_devices():
    # Can't pickle tKinter objects. Need to convert xpos, ypos, and image to dict
    devices_to_pickle = []
    for d in floor_plan_devices:
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


selected_device = None
save_button = tk.Button(root, text="Save", command=save_devices)
# self.save_button.pack(pady=20)
save_button.grid(row=3, rowspan=1, column=10, columnspan=1)
new_device_button = classes_testing.NewDeviceButton(canvas, root, all_devices)
# classes.DeleteDeviceButton(program_canvas.canvas)

# Load floorplan
if path.exists("saved_locations/devices.pk1"):
    classes_testing.FloorPlan(canvas, "apartment.png")
else:
    classes_testing.FloorPlan(canvas, "apartment.png")

# Load devices
if path.exists("saved_locations/devices.pk1"):
    pickle_in = open("saved_locations/devices.pk1", "rb")
    saved_devices = pickle.load(pickle_in)
    for d in saved_devices:
        all_devices.append(classes_testing.DeviceIcon(canvas,
                                              d['image_path'].split("/")[-1:][0],
                                              d['xpos'],
                                              d['ypos'],
                                              # root,
                                              d['device_name']))
else:
    print("No Devices on the floorplan")
    # self.alert_message.config(text="No devices on this floorplan")

print("running here")
setup_testing.root.mainloop()
