# import tkinter as tk
import floorplan_icons
from setup import *
import pickle
from PIL import ImageTk, Image
import os.path
from os import path

# root = tk.Tk()
# root.title('Inventory Locations')
# # root.iconbitmap("\\images\\greeen_circle.png")
# root.geometry("800x600")
#
# all_devices = []
# w = 600
# h = 400
# # Starting coordinates of the circle
# x = w//2
# y = h//2


# Likely going to be the layout of the floorplan
# canvas = tk.Canvas(root, width=w, height=h, bg="white")
canvas.pack(pady=20)
# device_icon = canvas.create_oval(x, y, x+10, y+10, fill="green")
# device_icon_green = canvas.create_image(x, y, image=img)

# img = tk.PhotoImage(file="images\\green_circle.png")
# floorplan_path = IMAGE_PATH + LAYOUTS_PATH + "apartment.png"
# apt_img = tk.PhotoImage(file=floorplan_path, )
# canvas.create_image(1, 1, image=apt_img)

# USING PILLOW TO RESIZE IMAGE
# Open Image
my_pic = Image.open(IMAGE_PATH + LAYOUTS_PATH + "apartment.png")

# Resize Image to the width and height of the canvas
resized = my_pic.resize((w, h), Image.ANTIALIAS)

# Make the resized pic into a PhotoImage
new_pic = ImageTk.PhotoImage(resized)

# Place image in canvas anchored to nw so it fills the whole canvas size
canvas.create_image(0, 0, anchor="nw", image=new_pic)


# def new_icon(e):
#     print(e.x)
#     print(e.y)
#     global canvas
#     # floorplan_icons.DeviceIcon(new_x=e.x, new_y=e.y, img=img, canvas=canvas)
#     floorplan_icons.DeviceIcon(canvas, "green_circle.png", e.x, e.y)

def move(e):
    global img
    img = tk.PhotoImage(file="images\\green_circle.png")
    print(e.x)
    print(e.y)
    # if x-20 >= e.x <= x+20 and y-20 >= e.y <= y+20:
    device_icon_green = canvas.create_image(e.x, e.y, image=img)
        # device_icon = canvas.create_oval(e.x-5, e.y-5, e.x+5, e.y+5, fill="green")
        # canvas.move(device_icon)
        # canvas.create_oval(e.x-5, e.y-5, e.x+5, e.y+5, fill="green")
    my_label.config(text="Coordinates  x: " + str(e.x) + " | y: " + str(e.y))
    # circle_label.config(text="Circle Coordinates x: " + str(device_icon_green.getattr(x)) + "  y: " + str(device_icon_green.getattr(y)))


# circle_label = tk.Label(root, text="")
# circle_label.pack(pady=50)
# my_label = tk.Label(root, text="")
# my_label.pack(pady=20)

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
new_device_button = tk.Button(root, text="Add Device", command=add_device)
new_device_button.pack(padx=30)
# B1-Motion is when button one is pressed on mouse
# canvas.bind("<B1-Motion>", move)
# canvas.bind("<Button 1>", new_icon)


if path.exists("saved_locations/devices.pk1"):
    pickle_in = open("saved_locations/devices.pk1", "rb")
    saved_devices = pickle.load(pickle_in)
    for d in saved_devices:
        all_devices.append(floorplan_icons.DeviceIcon(canvas,
                                                      d['image_path'].split("/")[-1:][0],
                                                      d['xpos'],
                                                      d['ypos']))

    print(saved_devices)
else:
    ypos = 150
    while ypos < 400:
        all_devices.append(floorplan_icons.DeviceIcon(canvas, "green_circle.png", 100, ypos))
        ypos += 100

# canvas.bind("<Enter>", print_true)

# DeviceIcon(root).pack(side="top", fill="both", expand="true")

root.mainloop()
