import glob
from PIL import Image

rawimagesfolder = "/tmp/dnimages/full/*"

width = 4
height = 8

filenames = glob.glob(rawimagesfolder)

if len(filenames) -  width*height >= 0:
    single_image_width, single_image_height = Image.open(filenames[0]).size

    collage = Image.new("RGB", (single_image_width * width, single_image_height * height), "white")

    for x in range(width):
        for y in range(height):
            left = x * single_image_width
            top = y * single_image_height
            image = Image.open(filenames.pop())
            collage.paste(image, (left,top))

    collage.save("/tmp/collage.jpg")

else:
    print "Not enough images for a collage with these dimensions"
