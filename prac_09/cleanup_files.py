"""
CP1404/CP5632 Practical
Clean up file names
"""
import os

SPECIAL_CHARACTERS = ['(']


def main():
    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Process all directories
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # Rename the files using the get_fixed_filename function
        for filename in filenames:
            current_file = os.path.join(directory_name, filename)
            new_name = get_fixed_filename(current_file)
            os.rename(current_file, new_name)


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
        else:
            new_name = new_name + current_letter
    for i, current_letter in enumerate(new_name):
        if current_letter == "_":
            new_name = new_name[:i + 1] + new_name[i + 1:].capitalize()
    return new_name


main()
