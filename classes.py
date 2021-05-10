# I need to make an object here that will be able to be drawn on the canvas make a computer class
# and it will be a green circle that you an move around but only if you click where the circle is
import tkinter as tk
# from global_variables import *
import global_variables
# from setup import *
from PIL import ImageTk, Image
import os
# from setup import IMAGE_PATH
# from main import canvas


class DeviceIcon(object):

    def __init__(self, canvas, image_name, xpos, ypos, root, device_name):
        # This is the same variable in memory as root. So it shouldn't be creating a bunch of new variables
        self.root = root
        # print(self.root.selected_device)
        self.canvas = canvas
        self.image_name = image_name
        self.device_name = device_name
        self.xpos, self.ypos = xpos, ypos

        self.tk_image = tk.PhotoImage(
            file="{}{}".format(global_variables.IMAGE_PATH + global_variables.DEVICE_ICONS_PATH, image_name))
        self.image_obj = canvas.create_image(
            xpos, ypos, image=self.tk_image)
        self.image_path = global_variables.IMAGE_PATH + global_variables.DEVICE_ICONS_PATH + image_name

        self.canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
        self.canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
        self.canvas.tag_bind(self.image_obj, '<Button-1>', self.clicked)
        self.move_flag = False

    def move(self, event):
        if self.move_flag:
            new_xpos, new_ypos = event.x, event.y

            self.canvas.move(self.image_obj,
                             new_xpos - self.mouse_xpos, new_ypos - self.mouse_ypos)

            self.mouse_xpos = new_xpos
            self.mouse_ypos = new_ypos
        else:
            self.move_flag = True
            self.canvas.tag_raise(self.image_obj)
            self.mouse_xpos = event.x
            self.mouse_ypos = event.y

    def release(self, event):
        print(event.x, event.y)
        self.xpos, self.ypos = event.x, event.y
        self.move_flag = False

    def clicked(self, event):
        print("Device Selected - X: " + str(self.xpos) + " Y: " + str(self.ypos))
        print(self.device_name)
        global_variables.selected_device = self


class FloorPlan(object):
    def __init__(self, canvas, image_name):
        if image_name:
            # USING PILLOW TO RESIZE IMAGE
            # Open Image
            my_pic = Image.open(global_variables.IMAGE_PATH + global_variables.LAYOUTS_PATH + image_name)

            # Resize Image to the width and height of the canvas
            resized = my_pic.resize((global_variables.w, global_variables.h), Image.ANTIALIAS)

            # Make the resized pic into a PhotoImage
            new_pic = ImageTk.PhotoImage(resized)
            # When this is in a function you have to do canvas.image. unsure why.
            canvas.image = new_pic
            # Place image in canvas anchored to nw so it fills the whole canvas size
            canvas.create_image(0, 0, anchor="nw", image=new_pic)
        else:
            pass


class NewDeviceButton(object):
    def __init__(self, canvas, root, all_devices):
        self.canvas = canvas
        self.root = root
        self.all_devices = all_devices
        self.new_device_button = tk.Button(root, text="Add Device", command=self.toggle)
        # self.new_device_button.pack(padx=40)
        self.new_device_button.grid(row=2, rowspan=1, column=11, columnspan=1)
        self.clicked = False
        canvas.bind("<Button-1>", self.test)
        # print("CREATED BUTTON")

    def toggle(self):
        if self.clicked:
            self.clicked = False
            print("Turned Off")
        else:
            print("Turned On")

    def test(self, event):
        if self.clicked:
            self.device_name_window = tk.Toplevel(width=100, height=100)
            self.device_name_window.geometry("%dx%d%+d%+d" % (200, 100, 250, 125))
            self.device_name_window.title("Enter name of device")
            self.device_name_entry = tk.Entry(master=self.device_name_window)
            # device_name.grid(row=0, column=0, columnspan=2)
            self.device_name_entry.pack(pady=10)
            add_name_button = tk.Button(master=self.device_name_window, text="Add Device", command=lambda: self.get_value(event))
            # add_name_button.grid(row=1, column=0, columnspan=1)
            add_name_button.pack()
            cancel_button = tk.Button(master=self.device_name_window, text="Cancel", command=self.device_name_window.destroy)
            # cancel_button.grid(row=1, column=1, columnspan=1)
            cancel_button.pack()
            # self.floor_plan_devices.append(DeviceIcon(self.canvas,
            #                                    "green_circle.png",
            #                                    event.x,
            #                                    event.y,
            #                                    self.root,
            #                                    device_name))
            self.toggle()

    def get_value(self, event):
        device_name = self.device_name_entry.get()
        print(str(event.x) + " | " + str(event.y))
        self.device_name_window.destroy()
        print(device_name)
        self.all_devices.append(DeviceIcon(self.canvas,
                                           "green_circle.png",
                                           event.x,
                                           event.y,
                                           self.root,
                                           device_name))


class FloorPlanList(object):
    def __init__(self, root):
        self.root = root
        self.floor_plan_listbox = tk.Listbox(self.root)
        self.floor_plan_listbox.grid(row=11, rowspan=4, column=0, columnspan=3)

    def add_all_floor_plans(self, floor_plan_list):
        for p in floor_plan_list:
            self.floor_plan_listbox.insert(tk.END, p)


class MessageLabel(object):
    def __init__(self, message):
        self.message = message
        self.message_label = tk.Label(self.root, text=self.message)
        # self.message_label.pack(pady=60)
        self.message_label.grid(row=12, rowspan=1, column=1, columnspan=1)
        print("GOT HERE")


# TODO: make a delete device button
# class DeleteDeviceButton(object):
#     def __init__(self, canvas):
#         self.delete_device_button = tk.Button(self.root, text="Delete Device", command=self.delete_device)
#         self.delete_device_button.pack(padx=60)
#
#         print("CREATED BUTTON")
#
#     def delete_device(self):
#         if program_canvas.selected_device:
#             print("Will delete device " + str(program_canvas.selected_device))
#         else:
#             print("No device selected")
