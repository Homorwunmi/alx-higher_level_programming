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

    """Initialize an empty string and itirate over the text"""
    formatted_text = ""
    s = 0
    while s < len(text):
        formatted_text += text[s]

        """
        Check if current character is one of the specified punctuation marks
        """
        if text[s] in ".?:":
            formatted_text += "\n\n"
            """Skip all following spaces"""
            s += 1
            while s < len(text) and text[s] == ' ':
                s += 1
            continue
        s += 1
