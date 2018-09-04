"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # Create new car object called limo with 100 units of fuel
    limo = Car("Limo", 100)
    # Add 20 units of fuel
    limo.add_fuel(20)
    # Print amount of fuel in car
    print(limo.fuel)
    # Attempt to drive 115km
    limo.drive(115)
    # Print odometer
    print(limo.odometer)
    # Print details using __str__ method
    print(limo)


main()
