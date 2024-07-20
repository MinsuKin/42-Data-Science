def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """Returns the BMI of each person in the list."""

    if len(height) != len(weight):
        exit("Error: the lists are not the same size")
    bmi = []
    for i in range(len(height)):
        if type(height[i]) is not int and type(height[i]) is not float:
            exit(f"Error: height[{i}] is not an integer or float")
        if type(weight[i]) is not int and type(weight[i]) is not float:
            exit(f"Error: weight[{i}] is not an integer or float")
        bmi.append(weight[i] / height[i] ** 2)
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a list of booleans based on the BMI and the limit."""

    return [True if i > limit else False for i in bmi]


def main():
    height = [2.71, 1.15, "a"]
    weight = [165.3, 38.4, "a"]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
