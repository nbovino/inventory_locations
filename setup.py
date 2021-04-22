import tkinter as tk

IMAGE_PATH = "images/"
root = tk.Tk()
root.title('Inventory Locations')
# root.iconbitmap("\\images\\greeen_circle.png")
root.geometry("800x600")

all_devices = []
w = 600
h = 400
# Starting coordinates of the circle
x = w//2
y = h//2

canvas = tk.Canvas(root, width=w, height=h, bg="white")