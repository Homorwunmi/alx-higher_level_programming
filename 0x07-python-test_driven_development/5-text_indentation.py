#!/usr/bin/python3

"""
Defines a text-indentation function.
"""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' and ':'
    Args:
        text (str): The text to print.
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = 0
    while s < len(text) and text[s] == ' ':
        s += 1

    while s < len(text):
        print(text[s], end="")
        if text[s] == "\n" or text[s] in ".?:":
            if text[s] in ".?:":
                print("\n")
            s += 1
            while s < len(text) and text[s] == ' ':
                s += 1
            continue
        s += 1
