import os

floor_plan_devices = []
floor_plans = []

selected_device = None
current_floor_plan = None
devices_movable = False
made_changes = False

IMAGE_PATH = "images/"
LAYOUTS_PATH = "layouts/"
DEVICE_ICONS_PATH = "device_icons/"
w = 600
h = 400
# Starting coordinates of the circle
x = w // 2
y = h // 2

for root, dir, file in os.walk(IMAGE_PATH + LAYOUTS_PATH):
    for f in file:
        floor_plans.append(f.split(".")[0])


