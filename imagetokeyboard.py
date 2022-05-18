from typing import List, Tuple
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter


def image_to_wooting_sized_buffer(fileName: str) -> List[List[List[int]]]:
    # applying many filters so that way it actually looks like stuff on the keyboard.
    # without sufficient brightness and contrast, everything just looks grey and boring.
    img = Image.open(fileName)
    color_filter = ImageEnhance.Color(img)
    img = color_filter.enhance(3.1)
    brightness_filter = ImageEnhance.Brightness(img)
    img = brightness_filter.enhance(1.3)
    img = img.filter(ImageFilter.GaussianBlur(radius=48))
    # uncomment this to see what you're actually basing your keyboard colors off of
    # img.show()

    # this line looks insane but i swear i know what i'm doing bro
    rtrn = list(list())

    w = img.width

    h = img.height

    for i in range(21):
        for j in range(6):
            pixel = img.getpixel((((w/21) * i) + w/42, ((h/6) * j) + h/12))
            rtrn.append(list(pixel))
    return rtrn
