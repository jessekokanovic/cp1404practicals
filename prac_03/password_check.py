"""
Checks password for minimum characters.
"""

MIN_LENGTH = 3

password = input("Choose password: ")
length = len(password)
while length < MIN_LENGTH:
    password = input("Password must be longer than {} characters: ".format(MIN_LENGTH))
    length = len(password)
print("*" * length)
