import random

quick_picks = []
MAXIMUM = 45
MINIMUM = 1

number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    quick_picks = []
    for j in range(6):
        random_number = random.randint(MINIMUM, MAXIMUM)
        while random_number in quick_picks:
            random_number = random.randint(MINIMUM, MAXIMUM)
        quick_picks.append(random_number)
    quick_picks.sort()
    print(" ".join("{:2}".format(number) for number in quick_picks))



