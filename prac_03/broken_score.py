"""
CP1404/CP5632 - Practical
Broken program to determine score status using functions.
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid Score")
if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
