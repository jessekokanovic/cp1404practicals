# count to 100 in 10s
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# count down from 20 to 1 in 1s
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Print n number of stars on one line
number_of_stars = int(input("How many stars: "))
for i in range(number_of_stars):
    print('*', end='')
print()

# Print stars on each line starting from 1 increasing to the nth
for i in range(number_of_stars):
    print('* ' * (i + 1))






