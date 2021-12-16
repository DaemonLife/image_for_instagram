from PIL import Image, ImageOps
import os

COLOR = "white"
BORDER_SIZE = 20
IMAGE_SIZE = 1080

# check existing two folders
arr = os.listdir()

square_is_exist = False
originals_is_exist = False
for line in arr:
    if line == "Square":
        square_is_exist = True
    if line == "Originals":
        originals_is_exist = True
    if (square_is_exist == True) and (originals_is_exist == True):
        break

if square_is_exist == False:
    os.makedirs("Square")
    print("Folder Square don't exist. Created now")
if originals_is_exist == False:
    os.makedirs("Originals")
    print("Folder Originals don't exist. Created now")

# take all photos from Originals
arr = os.listdir("./Originals")
images_arr = []

for line in arr:
    if (line[len(line)-4:] == ".jpg") or (line[len(line)-4:] == ".png"):
        images_arr.append(line)

all_images = len(images_arr)
i = 0
for line in images_arr:
    line = "./Originals/" + line
    i += 1
    # open image
    print(f"{i}/{all_images}: Working with {line}")
    img = Image.open(line)
    x, y = img.size

    if x > y:
        # * landscape
        new_x = IMAGE_SIZE - 2*BORDER_SIZE 
        new_y = int(y*new_x/x)
        size=(new_x,new_y)
        new_img = img.resize(size)
        border = (BORDER_SIZE, int((IMAGE_SIZE-new_y)/2), BORDER_SIZE, int((IMAGE_SIZE-new_y)/2))
        new_img = ImageOps.expand(new_img, border=border, fill=COLOR)

    else:
        # * portret or square
        new_y = IMAGE_SIZE - 2*BORDER_SIZE
        new_x = int(x*new_y/y)
        size=(new_x,new_y)
        new_img = img.resize(size)
        border = (int((IMAGE_SIZE-new_x)/2), BORDER_SIZE, int((IMAGE_SIZE-new_x)/2), BORDER_SIZE)
        new_img = ImageOps.expand(new_img, border=border, fill=COLOR)

    size=(IMAGE_SIZE,IMAGE_SIZE)
    new_img = new_img.resize(size)

    # save new image
    new_img.save("Square/"+line[12:]) # delete line path "./Originals"

print(f"Done!")
