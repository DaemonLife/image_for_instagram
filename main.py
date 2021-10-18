from PIL import Image, ImageOps
import os

arr = os.listdir()

folder_exist = False
for line in arr:
    if line == "Square":
        folder_exist = True
        break

if folder_exist == False:
    os.makedirs("Square")

for line in arr:
    if line[len(line)-4:] == (".jpg" or ".png"):

        # open image
        img = Image.open(line)

        # border color
        color = "white"

        x, y = img.size

        if x > y:
            # * landscape
            new_x = 1060
            new_y = int(y*new_x/x)
            size=(new_x,new_y)
            new_img = img.resize(size)
            border = (10, int((1080-new_y)/2), 10, int((1080-new_y)/2))
            new_img = ImageOps.expand(new_img, border=border, fill=color)

        else:
            # * portret or square
            new_y = 1060
            new_x = int(x*new_y/y)
            size=(new_x,new_y)
            new_img = img.resize(size)
            border = (int((1080-new_x)/2), 10, int((1080-new_x)/2), 10)
            new_img = ImageOps.expand(new_img, border=border, fill=color)

        size=(1080,1080)
        new_img = new_img.resize(size)

        # save new image
        new_img.save("Square/"+line)
