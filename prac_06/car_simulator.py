from prac_06.car import Car

MENU = """Menu:
d) Drive
r) Refuel
q) Quit"""
MENU_OPTIONS = ['d', 'r', 'q']


def main():
    print("Let's Drive!")
    car_name = input("Enter your car name: ")
    user_car = Car(car_name, 100)
    print(user_car)
    print(MENU)
    menu_selection = verify_user_choice(input("Enter your choice: ").lower())
    while menu_selection != 'q':
        if menu_selection == 'd':
            # Drive functionality
            distance_to_drive = int(input("How many km do you wish to drive? "))
            while distance_to_drive < 0:
                print("Distance must be >=0")
                distance_to_drive = int(input("How many km do you wish to drive? "))
            if distance_to_drive >= user_car.fuel:
                empty_tank_string = " and ran out of fuel"
                distance_to_drive = user_car.fuel
                user_car.drive(distance_to_drive)
            else:
                empty_tank_string = ""
                user_car.drive(distance_to_drive)
            print("The car drove {}km{}.\n".format(distance_to_drive, empty_tank_string))
            print(user_car)
            print(MENU)
            menu_selection = verify_user_choice(input("Enter your choice: ").lower())
        else:
            # Refuel functionality
            amount_to_refuel = int(input("How many units of fuel do you want to add to the car?"))
            while amount_to_refuel < 0:
                print("Fuel amount must be >= 0")
                amount_to_refuel = int(input("How many units of fuel do you want to add to the car?"))
            user_car.fuel = user_car.fuel + amount_to_refuel
            print("Added {} units of fuel.\n".format(amount_to_refuel))
            print(user_car)
            print(MENU)
            menu_selection = verify_user_choice(input("Enter your choice: ").lower())
    print("\nGoodbye {}'s driver".format(user_car.name))


def verify_user_choice(choice):
    while choice not in MENU_OPTIONS:
        print("Invalid Choice")
        print(MENU)
        choice = input("Enter your choice: ").lower()
    return choice


main()
