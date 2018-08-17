"""
CP1404/CP5632 - Practical
Broken program to determine score status using functions.
"""


def main():
    score = float(input("Enter score: "))
    score_category = check_score(score)
    print(score_category)


def check_score(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
