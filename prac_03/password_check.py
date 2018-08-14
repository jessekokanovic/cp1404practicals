"""
Checks password for minimum characters.
"""

MIN_LENGTH = 4


def main():
    password = get_password(MIN_LENGTH)
    return_asterisks(password)


def get_password(min_length):
    """Check if password meets length requirement."""
    password = input("Choose password: ")
    while len(password) < min_length:
        password = input("Password must be longer than {} characters: ".format(min_length))
    return password


def return_asterisks(length):
    """Print as many asterisks as there are characters in the password."""
    print("*" * len(length))


main()

