"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be
# The output will be 3
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return 0
    else:
        print(n ** 2)
        do_something(n - 1)


# TODO: 3. write down what you think the output of do_something(4) will be,
# It goes on forever, as it will call do_something(n - 1) which will forever - 1 from n and run.
# TODO: 4. use the debugger to step through and see what's actually happening
do_something(4)
# TODO: 5. fix do_something() so that it works according to the docstring


# Number of blocks needed for n rows in a pyramid
def calculate_number_of_blocks(n):
    """Sum the numbers from n to zero"""
    if n <= 0:
        return 0
    else:
        return n + calculate_number_of_blocks(n - 1)


print(calculate_number_of_blocks(6))
