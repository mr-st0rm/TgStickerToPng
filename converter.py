import os
from PIL import Image


def convert(photo_name: str) -> str:
    """
    Convert .webp to .png
    :param
    :photo_name = saved photo name
    :return saved .png photo name
    """

    new_png_name = f"{photo_name}.png"

    with Image.open(f'stickers/{photo_name}.webp') as img:
        img.convert('RGB')
        img.save(new_png_name, 'png')

    os.remove(f'stickers/{photo_name}.webp')
    return new_png_name
