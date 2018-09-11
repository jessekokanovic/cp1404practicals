from prac_06.car import Car

print("Let's Drive!")
car_name = input("Enter your car name: ")
user_car = Car(car_name, 100)

print(user_car)


distance_to_drive = int(input("How many km do you wish to drive? "))
while distance_to_drive < 0:
    print("Distance must be >=0")
    distance_to_drive = int(input("How many km do you wish to drive? "))
user_car.drive(distance_to_drive)
if user_car.odometer == 0:
    empty_tank_string = " and ran out of fuel"
else:
    empty_tank_string = ""

print("The car drove {}km{}.".format(distance_to_drive, empty_tank_string))

