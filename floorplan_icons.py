# I need to make an object here that will be able to be drawn on the canvas make a computer class
# and it will be a green circle that you an move around but only if you click where the circle is
import tkinter as tk
from main import root

class DeviceIcon(tk.Frame):
    def __init__(self, *args, **kwargs):
        self.x = x
        self.y = y
        self.img = tk.PhotoImage(file="images\\green_circle.png")
        self.device_icon_green = canvas.create_image(x, y, image=img)

        # tk.Frame.__init__(self, *args, **kwargs)
        # self.icon = tk.PhotoImage(file="images\\green_circle.png")
        # device_icon_green = canvas.create_image(x, y, image=img)
        # self.icon.bind("<Enter>", self.on_enter)
        # self.icon.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        # self.icon.configure(text="Hello world")
        pass

    def on_leave(self, enter):
        # self.icon.configure(text="")
        pass
