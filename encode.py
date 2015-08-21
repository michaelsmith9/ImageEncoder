#!/usr/bin/python

# import libraries of use
import sys
from PIL import Image
from PIL import *

# useful functions
def addBinary(array, data):
    """
    Takes an array and a number between 0 and 255 of data.
    Data is converted to binary form and appended to the array LSB first.
    """
    i = 0
    while i < 8:
        array.append((data & (2**i)) >> i)
        i += 1

# check the command line arguments
if len(sys.argv) != 3:
    print "Usage: ./encode.py imagename dataname"
    exit()

# get the imagename and dataname
imagename = sys.argv[1]
dataname = sys.argv[2]

# attempt to open image and data files
try:
    im = Image.open(imagename)
except:
    print "Could not open imagefile: ", imagename
    exit()

try:
    f = open(dataname, 'r')
except:
    print "Could not open datafile: ", dataname
    exit()

# we could open files, so let us begin...

# get the data, it will be a list of tuples (R,G,B) each 1 byte
data = im.getdata()

# create a new image
newImage = Image.new('RGB', im.size)

# get the width and height of the original image
(width, height) = im.size

# how many bytes of data can be store?
bytesAvailable = len(data)/8

# read the file
lines = f.readlines()

length = 0

for i in lines:
    length += len(i)

if length <= bytesAvailable:
    print "Enough space in image, proceeding with packing..."
else:
    print 'Insufficent room in image for file. Need ', length, ' bytes.'
    print 'There are ', bytesAvailable, ' bytes available'
    exit()

f.close()
im.close()

# create array of binary numbers representing ascii text
arr = []

for i in lines:
    for j in i:
        addBinary(arr, ord(j))

x = 0
y = 0

index = 0

stillgoing = True

# loop through all pixels
while y < height:
    x = 0
    while x < width:
        # get the pixel red, green and blue values 
        (R, G, B) = data[y*width + x]

        # cap index if we are past length
        
        if (index >= len(arr)):
            stillgoing = False

        if stillgoing == True:
            # get the current value at index
            # and set last bit of R to 1 if 1 and 0 if 0
            if arr[index] == 1:
                R2 = R | 0b00000001
            else:
                R2 = R & 0b11111110

            index += 1
            
            if index >= len(arr):
                break

            if arr[index] == 1:
                G2 = G | 0b00000001
            else:
                G2 = G & 0b11111110

            index += 1

            if index >= len(arr):
                break

            if arr[index] == 1:
                B2 = B | 0b00000001
            else:
                B2 = B & 0b11111110

            index += 1
        else:
            R2 = R
            G2 = G
            B2 = B

        # add the pixel to our new image
        newImage.putpixel((x, y), (R2, G2, B2))

        x += 1
    y += 1

# save our image
newImage.save('output.png', format='png')
