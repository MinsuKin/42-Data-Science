import sys

def main():
    if len(sys.argv) < 2:
        return
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    arg = sys.argv[1]
    try:
        number = int(arg)
    except Exception:
        raise AssertionError("argument is not an integer")

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")
