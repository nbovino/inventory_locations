# I need to make an object here that will be able to be drawn on the canvas make a computer class
# and it will be a green circle that you an move around but only if you click where the circle is
import tkinter as tk
from setup import *
from PIL import ImageTk, Image
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
        canvas.tag_bind(self.image_obj, '<Button-1>', self.clicked)
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
        program_canvas.alert_message.config(text="Device Selected - X: " + str(self.xpos) + " Y: " + str(self.ypos))


class FloorPlan(object):
    def __init__(self, canvas, image_name):
        # USING PILLOW TO RESIZE IMAGE
        # Open Image
        my_pic = Image.open(IMAGE_PATH + LAYOUTS_PATH + image_name)

        # Resize Image to the width and height of the canvas
        resized = my_pic.resize((w, h), Image.ANTIALIAS)

        # Make the resized pic into a PhotoImage
        new_pic = ImageTk.PhotoImage(resized)
        # When this is in a function you have to do canvas.image. unsure why.
        canvas.image = new_pic
        # Place image in canvas anchored to nw so it fills the whole canvas size
        canvas.create_image(0, 0, anchor="nw", image=new_pic)


class NewDeviceButton(object):
    def __init__(self, canvas):
        self.new_device_button = tk.Button(program_canvas.root, text="Add Device", command=self.toggle)
        self.new_device_button.pack(padx=40)
        self.clicked = False
        canvas.bind("<Button-1>", self.test)
        print("CREATED BUTTON")

    def toggle(self):
        if self.clicked:
            self.clicked = False
            print("Turned Off")
        else:
            self.clicked = True
            print("Turned On")

    def test(self, event):
        if self.clicked:
            all_devices.append(DeviceIcon(program_canvas.canvas,
                                          "green_circle.png",
                                          event.x,
                                          event.y))
            self.toggle()


class MessageLabel(object):
    def __init__(self, message):
        self.message = message
        self.message_label = tk.Label(program_canvas.root, text=self.message)
        self.message_label.pack(pady=60)
        print("GOT HERE")
