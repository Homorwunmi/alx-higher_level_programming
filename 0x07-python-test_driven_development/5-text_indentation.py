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

    """Initialize an empty string to store the result"""
    result = ""
    """Iterate through each character in the input text"""
    s = 0
    while s < len(text):
        result += text[s]
        if text[s] in ".?:":
            result += "\n\n"
            """Skip any following spaces"""
            s += 1
            while s < len(text) and text[s] == ' ':
                s += 1
            continue
        s += 1

    print(result, end='')
