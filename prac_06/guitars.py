from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
guitar_name = input("Name: ")
while guitar_name != "":
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: "))
    new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    guitars.append(new_guitar)
    print(new_guitar, "added.")
    guitar_name = input("\nName: ")

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("\nThese are my  guitars:")

for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:<15} ({}), worth ${:.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
