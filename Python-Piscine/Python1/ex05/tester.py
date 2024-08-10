import matplotlib.pyplot as plt

from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey


def main():
    array = ft_load("landscape.jpg")

    image_array = ft_invert(array)
    # image_array = ft_red(array)
    # image_array = ft_green(array)
    # image_array = ft_blue(array)
    # image_array = ft_grey(array)

    print(ft_invert.__doc__)

    plt.imshow(image_array)
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
