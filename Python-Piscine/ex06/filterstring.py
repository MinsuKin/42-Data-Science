import sys
from ft_filter import ft_filter


def LenAndAlnumFilter(text, size):
    """Filter words in text that are longer than size and
    contain only alphanumeric characters."""
    for word in text.split():
        if not word.isalnum():
            raise AssertionError("the arguments are bad")

    res = ft_filter(lambda word: len(word) > size, text.split())
    return res


def main():
    if len(sys.argv) == 3:
        text = sys.argv[1]
        if sys.argv[2].isdigit():
            size = int(sys.argv[2])
        else:
            raise AssertionError("the arguments are bad")
    else:
        raise AssertionError("the arguments are bad")

    filtered_text = LenAndAlnumFilter(text, size)

    print(filtered_text)


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
