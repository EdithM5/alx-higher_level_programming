#!/usr/bin/python3
""" defining a function that inserts line of text"""


def append_after(filename="", search_string="", new_string=""):
    """
    this funcion will find a string(search_string)
    and insert(new_string) on a new line after it
    all this is done in the file - filename
    """
    with open(filename, 'r+') as file:
        # Read the file line by line
        lines = file.readlines()
        # Go to the beginning of the file
        file.seek(0)
        # Write each line back to the file
        for line in lines:
            # If search string is in line, write the new string after it
            if search_string in line:
                file.write(line)
                file.write(new_string)
            else:
                file.write(line)
        # Truncate the file to remove any remaining content
        file.truncate()
