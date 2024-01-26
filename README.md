# Image Cryptography Tool
# Project Overview
This cryptography tool takes into input 2 images: 1) a secret image you wish to hide; 2) a container image in which to hide your hidden image.

Example of a secret image to hide:

![image to hide](https://github.com/RealMaximeCaloz/Portfolio/blob/7b6f6c8bc71cd3dca12de19d0a39c66480079096/epiccar.jpg)

Example of a container image in which to hide your hidden image:

![container image](https://github.com/RealMaximeCaloz/Portfolio/blob/7b6f6c8bc71cd3dca12de19d0a39c66480079096/basiccar.jpg)

This image cryptography tool uses bitwise operations to hide one image within the other.
All the pixels of each image are represented by an 8-bit binary number. However, the 4 first bits are more significant in terms of image recognition than the 4 last bits of an image.

For example, if you had a pixel represented by the binary number 10101111, 1010 would be the 4 most significant bits (MSB) and 1111 would be the 4 least significant bits (LSB).

If you truncated the last 4 bits (LSB), and ended up with 10100000 as the value of that given pixel, it would still look rather similar.

However, if you truncated only the 4 first bits (MSB), and ended up with 00001111 as the value of the given pixel, it would look different; this is especially true when the MSB truncation applied to all pixels of an image.

The significance of MSBs is the main concept used to make this image cryptography tool work.

In fact, we can conserve only the MSBs of both the image to hide, and the container image, in order to keep the main image information for both.

Then, we can place the hidden image's 4 MSBs in the LSB positions of the container image, thus generating a hybrid binary number which "contains" both the hidden and the container image.
Since the MSBs of this hybrid binary number belong to the container image, the hybrid, combined image will look a lot like the non-truncated hybrid image. Conversely, since the hidden image's MSBs are in the LSB positions of the hybrid binary number, the details of the hidden image will be very hard to see on the combined image (nearly invisible).

After running this software, you obtain such combined image which contains the hidden image, but as shown below, it looks very much like the unmodified container image.

Example of the combined image, which contains the hidden image:

![combined image](https://github.com/RealMaximeCaloz/Portfolio/blob/7b6f6c8bc71cd3dca12de19d0a39c66480079096/composite-image-with-hidden-image.jpg)

To the unsuspecting eye, the combined image and the non-truncated container image are exactly the same.

However, with an extraction algorithm provided in this software, one can extract the LSB-truncated version of the hidden image, from this combined image.

The extractor truncates the combined image's 4 MSBs, and shift the 4 LSBs (corresponding to the hidden image MSBs) to the left, such that they are in the MSB positions. Zeroes are added to the LSB positions.
Once this new binary number is shown, we effectively obtain a close representation of the original, non-truncated hidden image, as shown below:

Example of the hidden image extracted from the combined image:

![extracted image](https://github.com/RealMaximeCaloz/Portfolio/blob/7b6f6c8bc71cd3dca12de19d0a39c66480079096/hidden-image-extracted-from-composite.jpg)

As you can see, the extracted hidden image has inherited a few visual artefacts.

However, its depiction is still blatantly obvious, despite having been secretly cloaked in a completely different image.

This software is useful for transmittng secret images from one party to another party which knows the hidden image extraction algorithm, without a third party handling the combined image even knowing the hidden image is cloaked within it.


# Installation
1. Clone this repository:
```
$ git clone https://github.com/RealMaximeCaloz/Commercial-Bulk-Instagram-Post-Generator.git
```
2. Install the required python libraries:
```
$ pip install Pillow
$ pip install numpy
```

# How to Run
1. Find an image you want to hide, and a container image in which to hide the first image. Make sure both images have the same pixel dimensions. Place those images in the project folder.
2. Add your iamge names to `line 60` for the visible container image, and `line 69` for the hidden image.
3. Run `steganography.py`.
4. The first image, the container image, will pop-up on screen. Close it, and the image to hide will pop up next. Close it, and the combined image will appear (container image with the image to hide cloaked inside it). Finally, close the combined image, and the hidden image extracted from the combined image will pop up. All these images will be saved to the project folder.
