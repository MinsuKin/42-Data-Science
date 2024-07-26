from PIL import Image
import numpy


def ft_load(path: str):
    """This function takes a path to an image and returns a numpy array."""

    with Image.open(path) as img:
        img_rgb = img.convert("RGB")
        img_array = numpy.array(img_rgb)
        print(f"The shape of image is: {img_array.shape}")
        print(img_array)

        return img_array
