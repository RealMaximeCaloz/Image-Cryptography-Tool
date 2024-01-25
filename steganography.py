# Import PIL libary for image processing and numpy for math operations
from PIL import Image
import PIL
import numpy as np

# Method to obtain the 4 least significant digits of a binary number
def get_4_lsb(number):
    return number & 0b00001111

# Method to obtain the 4 most significant digits of a binary number
def get_4_msb(number):
    return (number & 0b11110000)

# Method to combine two sets of 4 bits into 1 binary number with 8 bits
def combine_bits(number1, number2):
    res = ((number1) | (number2>>4))
    return res

# Method to extract
def extract_image_values(image: PIL.Image):
  # Input: PIL image
  # Convert the PIL image information into a NumPy Array
  return np.array(image)

# Method to hide 1 image within a 2nd image.
# The method outputs a combined image which looks a lot like the visible image, but with a loss of detail, due to bit truncation.
def hide_image(img1, img2):
  # Input: two images of the same size, img1 and img2
    # The pixel values are extracted for each input
    img1_pixels = extract_image_values(img1)
    img2_pixels = extract_image_values(img2) 
    # vis = visible-image
    for x in range(vis_width):
        for y in range(vis_height):
                for z in range(3):
                  # the visible image's 4 MSB are combined with the hidden image's 4 MSB.
                  # the hidden image's 4 MSB are placed in the visible image's 4 LSB.
                  # the visible image's 4 LSB are discarded.
                  img1_pixels[x,y,z] = combine_bits(get_4_msb(img1_pixels[x,y,z]),get_4_msb(img2_pixels[x,y,z]))
    return img1_pixels


# Method which extracts the hidden image from the combined image (combination of the visible and the hidden images)
# The method retuns an image which looks like the initial hidden image, but with a loss of detail due to truncation of bits
def recover_image(img):
  # Input: the image created using "hide_image(img1, img2)"
    img_pixels = extract_image_values(img)
    print(img_pixels)
    for x in range(vis_width):
        for y in range(vis_height):
            for z in range(3):
              pixel = int(img_pixels[x,y,z])
              img_pixels[x,y,z] = get_4_lsb(pixel)
              img_pixels[x,y,z] = img_pixels[x,y,z] << 4
    image = Image.fromarray(img_pixels)
    return image


#importing the "visible" image
visible_image = Image.open("basiccar.jpg")
visible_image.show()
print(visible_image)

print(visible_image.format,visible_image.size,visible_image.mode)

vis_width, vis_height = visible_image.size

#importing the "hidden" image
hidden_image = Image.open("epiccar.jpg")
hidden_image.show()
print(hidden_image.format,hidden_image.size,hidden_image.mode)

hidden_width, hidden_height = hidden_image.size

# Combining the visible and hidden images to create a combined image with the hidden image cloaked
new_img_pixels = hide_image(visible_image, hidden_image)
array = np.array(new_img_pixels, dtype=np.uint8)
print(array.shape)
new_image = Image.fromarray(array)
new_image.show()
new_image.save('./composite-image-with-hidden-image.jpg')

# Retrieving the hidden image from the combined image
new_image_rendered = recover_image(new_image)
new_image_rendered.show()
new_image_rendered.save('./hidden-image-extracted-from-composite.jpg')