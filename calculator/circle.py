import math

while True:
    print("-----------------------------------------------------------")
    print("Circle: ")
    print("formula: Area = ( π * [r]^2 )*([∮] / 360)")
    print("\'∮\' is a central angle ")

    r = float(input("r= "))
    e = float(input("∮= "))
    Area = (r ** 2) * math.pi * (e / 360)
    print("Area= ", Area, "/v")

    Back = input("Back to Area?\n( y / n ) :")
    if Back == "y":
        import area
