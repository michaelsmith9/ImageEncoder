#!/usr/bin/python

# import libraries to use 
import sys
from PIL import Image
from PIL import *

def convertBinaryToAscii(array):
    """
    Takes the array assumed to be ascii binary numbers and returns
    an array of ascii characters.
    """
    index = 0
    num = 0
    result = []
    for i in array:
        num += (2**((index)%8))*i
        index += 1
        if (index % 8) == 0 and index != 0:
            result.append(chr(num))
            num = 0
            index = 0

    return result

# check the command line args
if len(sys.argv) != 3:
    print "Usage: ./decode.py imagename outputname"
    exit()

# get the imagename and attempt to open
imagename = sys.argv[1]
fname = sys.argv[2]

try:
    im = Image.open(imagename)
except:
    print "Could not open imagefile: ", imagename
    exit()

# open the image
data = im.getdata()

(width, height) = im.size

darray = []

f = open(fname, 'w')

# for each pixel in data, get the LSB
for i in data:
    (R, G, B) = i
    darray.append((R & (1 << 0)))
    darray.append((G & (1 << 0)))
    darray.append((B & (1 << 0)))


# covnert the pixel data to ascii
result = convertBinaryToAscii(darray)

for i in result:
    f.write(i)

f.close()
