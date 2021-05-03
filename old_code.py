# Create line
# canvas.create_line(x1, y1, x2, y2, fill="color")
# canvas.create_line()

# Create rectangle
# x1, y1: top left
# x2, y2: bottom right
# canvas.create_rectangle(x1, y1, x2, y2, fill="color")

# root = tk.Tk()
# root.title('Inventory Locations')
# # root.iconbitmap("\\images\\greeen_circle.png")
# root.geometry("800x600")
#

# w = 600
# h = 400
# # Starting coordinates of the circle
# x = w//2
# y = h//2
#
# canvas = tk.Canvas(root, width=w, height=h, bg="white")
# canvas.pack(pady=20)

# Create Oval
# Same as rectangle, top left coordinate and bottom right coordinate
# canvas.create_oval(50, 150, 250, 50, fill="cyan")
# canvas.create_oval(50, 150, 250, 50, fill="cyan")

def move(e):
    # global img
    # img = tk.PhotoImage(file="images\\green_circle.png")
    print(e.x)
    print(e.y)
    # if x-20 >= e.x <= x+20 and y-20 >= e.y <= y+20:
    # device_icon_green = canvas.create_image(e.x, e.y, image=img)
        # device_icon = canvas.create_oval(e.x-5, e.y-5, e.x+5, e.y+5, fill="green")
        # canvas.move(device_icon)
        # canvas.create_oval(e.x-5, e.y-5, e.x+5, e.y+5, fill="green")
    # my_label.config(text="Coordinates  x: " + str(e.x) + " | y: " + str(e.y))
    # circle_label.config(text="Circle Coordinates x: " + str(device_icon_green.getattr(x)) + "  y: " + str(device_icon_green.getattr(y)))


# circle_label = tk.Label(root, text="")
# circle_label.pack(pady=50)
# my_label = tk.Label(root, text="")
# my_label.pack(pady=20)

# USING PILLOW TO RESIZE IMAGE
# Open Image
# my_pic = Image.open(IMAGE_PATH + LAYOUTS_PATH + "apartment.png")

# Resize Image to the width and height of the canvas
# resized = my_pic.resize((w, h), Image.ANTIALIAS)

# Make the resized pic into a PhotoImage
# new_pic = ImageTk.PhotoImage(resized)

# Place image in canvas anchored to nw so it fills the whole canvas size
# canvas.create_image(0, 0, anchor="nw", image=new_pic)


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