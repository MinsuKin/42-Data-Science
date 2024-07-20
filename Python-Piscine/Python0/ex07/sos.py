import sys

NESTED_MORSE = {
        "A": ".-", "B": "-...", "C": "-.-.",
        "D": "-..", "E": ".", "F": "..-.",
        "G": "--.", "H": "....", "I": "..",
        "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.",
        "S": "...", "T": "-", "U": "..-",
        "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..",
        "9": "----.",
        " ": "/ "
    }


def ConvertToMorse(text):
    """Converts a string to morse code."""
    morse_code = ""
    for char in text:
        if char.isalnum() or char.isspace():
            morse_code += NESTED_MORSE[char.upper()] + " "
        else:
            raise AssertionError("the arguments are bad")

    return morse_code.rstrip()


def main():
    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        raise AssertionError("the arguments are bad")

    morse_code = ConvertToMorse(text)

    print(morse_code)


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
