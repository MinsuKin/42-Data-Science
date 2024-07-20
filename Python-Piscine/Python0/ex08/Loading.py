import os
import sys


def ft_tqdm(lst: range) -> None:
    """A simple tqdm implementation."""
    total = len(lst)
    terminal_width = os.get_terminal_size().columns
    bar_width = terminal_width - 40

    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    for index, elem in enumerate(lst):
        percent = (index + 1) / total
        progress = int(bar_width * percent)
        bar = ('█' * progress).ljust(bar_width)

        percent_str = f"{int(percent * 100):>3}%"
        sys.stdout.write(f"\r{percent_str}|{bar}| {index + 1}/{total}")
        sys.stdout.flush()
        yield elem
