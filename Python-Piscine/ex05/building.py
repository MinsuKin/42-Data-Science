import sys
import string


def count_uppercase(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    return count


def count_lowercase(text):
    count = 0
    for char in text:
        if char.islower():
            count += 1
    return count


def count_punctuation(text):
    count = 0
    for char in text:
        if char in string.punctuation:
            count += 1
    return count


def count_digits(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count


def count_spaces(text):
    count = 0
    for char in text:
        if char.isspace():
            count += 1
    return count


def analyze_text(text):
    num_uppercase = count_uppercase(text)
    num_lowercase = count_lowercase(text)
    num_punctuation = count_punctuation(text)
    num_digits = count_digits(text)
    num_spaces = count_spaces(text)

    return {
        "length": len(text),
        "uppercase": num_uppercase,
        "lowercase": num_lowercase,
        "punctuation": num_punctuation,
        "digits": num_digits,
        "spaces": num_spaces
    }


def main():
    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        raise AssertionError("Only one argument is allowed")

    analysis = analyze_text(text)

    print(f"The text contains {analysis['length']} characters:")
    print(f"{analysis['uppercase']} upper letters")
    print(f"{analysis['lowercase']} lower letters")
    print(f"{analysis['punctuation']} punctuation marks")
    print(f"{analysis['spaces']} spaces")
    print(f"{analysis['digits']} digits")


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        sys.exit(1)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
