import matplotlib.pyplot as plt
from load_image import ft_load, convert_to_grayscale


def zoom_image(image_array):
    """Zoom into the center of the image by the specified zoom factor."""

    height, width = image_array.shape
    center_x, center_y = width // 2, height // 2

    offset_x, offset_y = 140, 85
    center_x += offset_x
    center_y -= offset_y

    new_width, new_height = 400, 400
    start_x, start_y = center_x - new_width // 2, center_y - new_height // 2
    end_x, end_y = start_x + new_width, start_y + new_height

    zoomed_image = image_array[start_y:end_y, start_x:end_x]
    print(f"New shape after slicing: {zoomed_image.shape}")
    print(zoomed_image)

    return zoomed_image


def display_image(image_array):
    """Display the image."""

    plt.gray()
    plt.imshow(image_array)
    plt.show()


def main():
    img_array = ft_load("animal.jpeg")
    img_array = convert_to_grayscale(img_array)

    if img_array is not None:
        zoomed_img = zoom_image(img_array)
        display_image(zoomed_img)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
