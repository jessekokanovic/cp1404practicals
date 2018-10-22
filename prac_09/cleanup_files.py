"""
CP1404/CP5632 Practical
Clean up file names
"""
import os

SPECIAL_CHARACTERS = ['(']


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    get_fixed_filename("The FirstNoel(remix).TXT")
    # for filename in os.listdir('.'):
    #     get_fixed_filename(filename)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    for index, current_letter in enumerate(filename):
        try:
            next_letter = filename[index + 1]
        except IndexError:
            pass
        if current_letter.islower() and next_letter.isupper():
            new_name = new_name + current_letter + "_"
        elif current_letter in SPECIAL_CHARACTERS:
            new_name = new_name + "_" + current_letter
        elif current_letter.isspace():
            new_name = new_name + "_"
        else:
            new_name = new_name + current_letter
    new_name = new_name.replace(".TXT", ".txt")
    return new_name


main()
