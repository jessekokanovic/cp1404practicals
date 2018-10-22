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
    print(get_fixed_filename("The firstNoel(remix).TXT"))
    # for filename in os.listdir('.'):
    #     print(get_fixed_filename(filename))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    filename = filename.replace(".TXT", ".txt")
    for index, current_letter in enumerate(filename):
        try:
            next_letter = filename[index + 1]
            previous_letter = filename[index - 1]
        except IndexError:
            pass
        if (current_letter.islower() and next_letter.isupper()) or (current_letter.isupper() and next_letter.isupper()):
            new_name = new_name + current_letter + "_"
        elif current_letter in SPECIAL_CHARACTERS and previous_letter.isalnum():
            new_name = new_name + "_" + current_letter
        elif current_letter.isspace():
            new_name = new_name + "_"
            print(filename[index + 1].upper())
        else:
            new_name = new_name + current_letter
    return new_name


main()
