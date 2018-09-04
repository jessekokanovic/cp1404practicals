COLOUR_TO_HEX = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4",
                 "azure1": "#f0ffff", "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000",
                 "blue1": "#0000ff", "BlueViolet": "#8a2be2", "brown": "#a52a2a"}

colour_choice = input("What Colour? ")
while colour_choice != "":
    print("The code for {} is {}".format(colour_choice, COLOUR_TO_HEX.get(colour_choice)))
    colour_choice = input("What Colour? ")
