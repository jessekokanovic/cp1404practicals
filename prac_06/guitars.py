from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
# guitar_name = input("Name: ")
# while guitar_name != "":
#     guitar_year = input("Year: ")
#     guitar_cost = input("Cost: ")
#     new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
#     guitars.append(new_guitar)
#     guitar_name = input("\nName: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("\nThese are my  guitars:\n")

for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {} ({}), worth ${:.2f}{}".format(i, guitar.name, guitar.year, guitar.cost, vintage_string))
