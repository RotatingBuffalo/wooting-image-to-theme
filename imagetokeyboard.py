from typing import List, Tuple
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter


def image_to_wooting_sized_buffer(fileName: str) -> List[List[List[int]]]:
    img = Image.open(fileName)
    img = img.filter(ImageFilter.GaussianBlur(radius=1000.5))
    color_filter = ImageEnhance.Color(img)
    img = color_filter.enhance(5.0)
    brightness_filter = ImageEnhance.Brightness(img)
    img = brightness_filter.enhance(2.0)

    img.show()

    # this line looks insane but i swear i know what i'm doing bro
    rtrn = list(list())

    w = img.width/2
    h = img.height - img.height/10
    for i in range(6):
        for j in range(21):
            pixel = img.getpixel((img.width/2 + (w - ((w/21) * j))-1,
                                  img.height/20 + (h - ((h/6) * i))-1))
            rtrn.append(list(pixel))
    return rtrn
