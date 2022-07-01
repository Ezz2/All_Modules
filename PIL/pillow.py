# By Ezz

# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------

from PIL import Image

# Open The Image
myImage = Image.open("D:\ezz.programing\python\Images\Ezz_Image.png")

# Show The Image
myImage.show()

# My Cropped Image
myBox = (0, 0, 400, 400) # Left, Upper, right, Lower
mynewImage = myImage.crop(myBox)

# Show The New Image
mynewImage.show()

# My Converted Mode Image
myConverted = myImage.convert("L")
myConverted.show()
