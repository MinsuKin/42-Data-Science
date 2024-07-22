from PIL import Image
import numpy


def ft_load(path: str):
    """This function takes a path to an image and returns a numpy array."""
    with Image.open(path) as img:
        img_rgb = img.convert("RGB")
        img_array = numpy.array(img_rgb)
        print(f"The shape of image is: {img_array.shape}")
        return img_array


def main():
    print(ft_load("landscape.jpg"))
    print(ft_load("landscape.jpeg"))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
