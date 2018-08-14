# 1. Write name to file
name = str(input("Name: "))
name_file = open("names.txt", 'w')
print(name, file=name_file)
name_file.close()

# 2. Reading from file
name_file = open("names.txt", 'r')
file_contents = name_file.read()
print('Your name is', file_contents)
name_file.close()

# 3. Read numbers and add them together
number_file = open("numbers.txt", 'r')
number1 = int(number_file.readline())
number2 = int(number_file.readline())
total = number1 + number2
print(total)
number_file.close()


# 3. extension
total = 0
number_file = open("numbers.txt", 'r')

for line in number_file:
    value = int(line)
    total = total + value
number_file.close()
print(total)




