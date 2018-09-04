from prac_06.guitar import Guitar

guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_2 = Guitar("Another Guitar", 2012, 169.95)

# Check if get_age works correctly
print(guitar_1.name, "- Expected 96. Got", guitar_1.get_age())
print(guitar_2.name, "- Expected 6. Got", guitar_2.get_age())

# Checks if is_vintage works correctly
print(guitar_1.name, "-Expected True. Got", guitar_1.is_vintage())
print(guitar_2.name, "-Expected False. Got", guitar_2.is_vintage())
