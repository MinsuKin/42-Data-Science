from PIL import Image
import numpy


def ft_load(path: str):
    """This function takes a path to an image and returns a numpy array."""

    with Image.open(path) as img:
        img_rgb = img.convert('L')
        img_array = numpy.array(img_rgb)

        return img_array
