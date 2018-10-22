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
    get_fixed_filename("TheFirstNoel.TXT")
    # for filename in os.listdir('.'):
    #     get_fixed_filename(filename)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name =""
    for index, current_letter in enumerate(filename):
        try:
            next_letter = filename[index + 1]
        except IndexError:
            pass
        print(current_letter)
        print(next_letter)
        if current_letter.islower() and next_letter.isupper():
            # new_name = new_name[:index + 1] + "_" + new_name[index + 1:]
            new_name = new_name + current_letter + "_"
            print(new_name)
        elif current_letter in SPECIAL_CHARACTERS:
            new_name = new_name[:index] + "_" + new_name[index:]
        elif current_letter.isspace():
            new_name = new_name[:index + 1].replace(" ", "_") + new_name[index + 1:]
    new_name = new_name.replace(".TXT", ".txt")

    return print(new_name)


main()
