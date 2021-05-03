import tkinter as tk
import classes

# root = tk.Tk()
# root.title('Inventory Locations')
# # root.iconbitmap("\\images\\greeen_circle.png")
# root.geometry("800x600")
#
all_devices = []

IMAGE_PATH = "images/"
LAYOUTS_PATH = "layouts/"
DEVICE_ICONS_PATH = "device_icons/"

w = 600
h = 400
# Starting coordinates of the circle
x = w // 2
y = h // 2


class BaseWindow(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Inventory Locations')
        # root.iconbitmap("\\images\\greeen_circle.png")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, width=w, height=h, bg="white")
        self.canvas.pack(pady=20)
        # self.canvas.grid(column=1)
        self.alert_message = tk.Label(self.root, text="HELLO")
        self.alert_message.pack(pady=30, side=tk.RIGHT)
        self.selected_device = None


program_canvas = BaseWindow()
