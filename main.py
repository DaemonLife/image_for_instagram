from PIL import Image, ImageOps
import os


IMAGE_SIZE = 1080
BORDER_SIZE = 20

arr = os.listdir()

folder_exist = False
for line in arr:
    if line == "Square":
        folder_exist = True
        break

if folder_exist == False:
    os.makedirs("Square")

i = 0

for line in arr:
    if line[len(line)-4:] == (".jpg" or ".png"):
        i += 1
        # open image
        print(f"{i}: Working with {line}")
        img = Image.open(line)

        # border color
        color = "white"

        x, y = img.size

        if x > y:
            # * landscape
            new_x = IMAGE_SIZE - 2*BORDER_SIZE 
            new_y = int(y*new_x/x)
            size=(new_x,new_y)
            new_img = img.resize(size)
            border = (BORDER_SIZE, int((IMAGE_SIZE-new_y)/2), BORDER_SIZE, int((IMAGE_SIZE-new_y)/2))
            new_img = ImageOps.expand(new_img, border=border, fill=color)

        else:
            # * portret or square
            new_y = IMAGE_SIZE - 2*BORDER_SIZE
            new_x = int(x*new_y/y)
            size=(new_x,new_y)
            new_img = img.resize(size)
            border = (int((IMAGE_SIZE-new_x)/2), BORDER_SIZE, int((IMAGE_SIZE-new_x)/2), BORDER_SIZE)
            new_img = ImageOps.expand(new_img, border=border, fill=color)

        size=(IMAGE_SIZE,IMAGE_SIZE)
        new_img = new_img.resize(size)

        # save new image
        new_img.save("Square/"+line)
        print(f"Done!")
        print()
