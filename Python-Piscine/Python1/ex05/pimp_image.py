import numpy
from numpy import ndarray as array


def ft_invert(array) -> array:
    """Inverts the color of the image received."""

    array[:, :, 0] = 255 - array[:, :, 0]
    array[:, :, 1] = 255 - array[:, :, 1]
    array[:, :, 2] = 255 - array[:, :, 2]

    return array


def ft_red(array) -> array:
    """Applies a red filter to the image received."""

    array[:, :, 1] = 0
    array[:, :, 2] = 0

    return array


def ft_green(array) -> array:
    """Applies a green filter to the image received."""

    array[:, :, 0] = 0
    array[:, :, 2] = 0

    return array


def ft_blue(array) -> array:
    """Applies a blue filter to the image received."""

    array[:, :, 0] = 0
    array[:, :, 1] = 0
    return array


def ft_grey(array) -> array:
    """Applies a grayscale filter to the image received."""

    weights = numpy.array([0.299, 0.587, 0.114])

    gray = numpy.dot(array[..., :3], weights)

    array[:, :, 0] = gray
    array[:, :, 1] = gray
    array[:, :, 2] = gray

    return array
