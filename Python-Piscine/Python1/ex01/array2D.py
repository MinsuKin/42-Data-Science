def slice_me(family: list, start: int, end: int) -> list:
    """Returns a slice of the 2D array."""

    if type(family) is not list:
        exit("Error: family is not a list")

    for row in family:
        if len(row) != len(family[0]):
            exit("Error: the rows are not the same size")

    print(f"My shape is : ({len(family)}, {len(family[0])})")
    sliced_family = family[start:end]
    print(f"My new shape is : ({len(sliced_family)}, {len(sliced_family[0])})")
    return sliced_family


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
