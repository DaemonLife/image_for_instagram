from PIL import Image, ImageOps

# open image
img = Image.open("img1.jpg")

# border color
color = "white"

# top, right, bottom, left
x, y = img.size

if x > y:
    print('landscape')
    new_x = 1080
    new_y = int(y*new_x/x)
    size=(new_x,new_y)
    new_img = img.resize(size)
    border = (0, int((1080-new_y)/2), 0, int((1080-new_y)/2))
    new_img = ImageOps.expand(new_img, border=border, fill=color)

else:
    print('portret')
    new_y = 1080
    new_x = int(x*new_y/y)
    size=(new_x,new_y)
    new_img = img.resize(size)
    border = (int((1080-new_x)/2), 0, int((1080-new_x)/2), 0)
    new_img = ImageOps.expand(new_img, border=border, fill=color)

size=(1080,1080)
new_img = new_img.resize(size)

# save new image
new_img.save("test2.jpg")
