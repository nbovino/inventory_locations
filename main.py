import tkinter as tk
import floorplan_icons
from setup import *
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
img = tk.PhotoImage(file="images\\green_circle.png")
# device_icon_green = canvas.create_image(x, y, image=img)


def new_icon(e):
    print(e.x)
    print(e.y)
    global canvas
    # floorplan_icons.DeviceIcon(new_x=e.x, new_y=e.y, img=img, canvas=canvas)
    floorplan_icons.DeviceIcon(canvas, "green_circle.png", e.x, e.y)

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


circle_label = tk.Label(root, text="")
circle_label.pack(pady=50)
my_label = tk.Label(root, text="")
my_label.pack(pady=20)
# B1-Motion is when button one is pressed on mouse
# canvas.bind("<B1-Motion>", move)
canvas.bind("<Button 1>", new_icon)
# canvas.bind("<Enter>", print_true)


# DeviceIcon(root).pack(side="top", fill="both", expand="true")

root.mainloop()
