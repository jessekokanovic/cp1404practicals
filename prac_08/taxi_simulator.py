from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)choose taxi, d)rive"
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
total_bill = 0

print("Lets drive!")
print(MENU)
menu_choice = input(">>>").upper()
while menu_choice != "Q":
    if menu_choice == "C":
        print("Taxis available:")
        for taxi_number, taxi in enumerate(taxis):
            print("{} - {}".format(taxi_number, taxi))
        chosen_taxi = int(input("Chosen taxi: "))
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>>")
    else:
        distance_to_drive = int(input("Drive how far?"))
        taxis[chosen_taxi].start_fare()
        taxis[chosen_taxi].drive(distance_to_drive)
        fare = taxis[chosen_taxi].get_fare()
        total_bill = total_bill + fare
        print("Your {} trip cost you ${}".format(taxis[chosen_taxi].name, fare))
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>>")
print("Total trip cost: ${}".format(total_bill))
print("Taxis are now:")
for taxi_number, taxi in enumerate(taxis):
    print("{} - {}".format(taxi_number, taxi))


