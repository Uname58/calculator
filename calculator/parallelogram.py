import math

while True:
    print("-----------------------------------------------------------")
    print("    .____________.")
    print("   /|           /")
    print("  / |h         /")
    print(" /__|_________/")
    print("        b")
    print("formula: Area = [h] * [b]")
    h = float(input("h= "))
    b = float(input("b= "))
    Area = h * b
    print("Area= ", Area, "\n")

    Back = input("Back to Area?\n( y / n ) :")
    if Back == "y":
        import area
