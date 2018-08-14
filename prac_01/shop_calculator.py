"""
Program to calculate the total cost of a shopper's items
Allow the user to input the number of items
Allow the user to enter the price for each item
Calculate total cost and apply discount if necessary
"""
total_cost = 0.0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print('Invalid number of items!')
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    total_cost = total_cost + float(input("Price of item {}: $".format(i+1)))
if total_cost > 100:
    total_cost = total_cost * 0.9
    print('Enjoy your 10% discount!')
print('Total cost for {} items is: ${:.2f}'.format(number_of_items, total_cost))

