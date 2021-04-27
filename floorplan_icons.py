# I need to make an object here that will be able to be drawn on the canvas make a computer class
# and it will be a green circle that you an move around but only if you click where the circle is
import tkinter as tk
from setup import *
# from setup import IMAGE_PATH
# from main import canvas


class DeviceIcon(object):
    def __init__(self, canvas, image_name, xpos, ypos):
        self.canvas = canvas
        self.image_name = image_name
        self.xpos, self.ypos = xpos, ypos

        self.tk_image = tk.PhotoImage(
            file="{}{}".format(IMAGE_PATH + DEVICE_ICONS_PATH, image_name))
        self.image_obj = canvas.create_image(
            xpos, ypos, image=self.tk_image)
        self.image_path = IMAGE_PATH + DEVICE_ICONS_PATH + image_name

        canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
        canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
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


# Testing from 4/20/21
# class DeviceIcon(tk.Frame):
#     def __init__(self, new_x, new_y, img, canvas):
#         self.x = new_x
#         self.y = new_y
#         self.img = img
#         self.canvas = canvas
#         self.device_icon_green = canvas.create_image(self.x, self.y, image=img)
#         all_devices.append(self)
#         for d in all_devices:
#             print(d.x, d.y)
#         self.canvas.bind("<B1-Motion>", self.move_image)
#
#     def move_image(self, event):
#         # delete the old image
#         self.canvas.delete(self.img)
#         # get the mouse position
#         x = event.x
#         y = event.y
#         # create the new image at position x, y
#         self.img = self.canvas.create_image(x, y, image=self.img)
#         self.canvas.update()




# Old device icon class
# class DeviceIcon(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         self.x = x
#         self.y = y
#         self.img = tk.PhotoImage(file="images\\green_circle.png")
#         self.device_icon_green = canvas.create_image(x, y, image=img)
#
#         # tk.Frame.__init__(self, *args, **kwargs)
#         # self.icon = tk.PhotoImage(file="images\\green_circle.png")
#         # device_icon_green = canvas.create_image(x, y, image=img)
#         # self.icon.bind("<Enter>", self.on_enter)
#         # self.icon.bind("<Leave>", self.on_leave)
#
#     def on_enter(self, event):
#         # self.icon.configure(text="Hello world")
#         pass
#
#     def on_leave(self, enter):
#         # self.icon.configure(text="")
#         pass
