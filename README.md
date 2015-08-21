# ImageEncoder
Steganography using Python
Plain text data (non-encrypted) is encoded into an image using steganography.
Two files are given at the moment (with the intention of extending the functionality to create a library). This repo was a proof of concept. 

“encode.py” takes an image file name and a data file name and modifies each pixel in the image file slightly to hide the data file within the image.
“decode.py” takes an image and attempts to decode it and produces the corresponding ascii text.

Encoding is performed by taking the (R, G, B) value for each pixel and modifying the LSB so that it corresponds to a 1 or a 0 bit in a byte.

There are many things to do from here including:
- creating a library of functions surrounding encoding, decoding, etc.
- encrypting data before writing it
- adding a beginning and end ‘signature’ to the image to recognise if it is valid data
