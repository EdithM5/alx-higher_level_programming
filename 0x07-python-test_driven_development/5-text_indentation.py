#!/usr/bin/python3
"""
defining a function that prints 2 new lines
after :, ?, . (not the commas)
"""


def text_indentation(text):
    """
    after : there should be 2 new lines
    after ? there should be 2 new lines
    after . there should be 2 new lines
    no white spaces before or after
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
    print("\n".join([line.strip() for line in new_text.split('\n')]))
