import time
import sys


def scroll_print(text):
    """Prints text 1 character at a time to simulate scrolling text.

    Args:
        text (str): The text to be printed.

    """
    count = 0

    for char in text:
        time.sleep(0.001)

        if count > 80 and char == ' ':
            count = 0
            sys.stdout.write('\n')
        else:
            sys.stdout.write(char)

        sys.stdout.flush()

        count += 1

    sys.stdout.write('\n')
    sys.stdout.flush()
