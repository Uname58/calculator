import math

while True:
    print("Basic Formula<---- 1\n")
    print("Sine  Formula<---- 2\n")
    print("Heron Formula<---- 3\n")
    print("Back to Area <---- !\n")
    MODE = input("Mode<----- ")

    if MODE == "1":
        print("-----------------------------------------------------------")
        print(" .")
        print(" |\\")
        print(" | \\")
        print("h|  \\")
        print(" |   \\")
        print(" |____\\")
        print("   b")
        print("formula: Area = ( [h] * [b] )/2")

        h = float(input("h= "))
        b = float(input("b= "))
        Area = h*b*1/2
        print("Area= ", Area, "\n=================================")
    elif MODE == "2":
        print("-----------------------------------------------------------")
        print("     .    ")
        print("    / \\  ")
        print(" a /   \\ ")
        print("  /     \\")
        print(" /_______\\ ")
        print("A    b    ")
        print("formula: Area = ( (1/2)*( [a] * [b] * sin[A] )")

        a = float(input("a= "))
        b = float(input("b= "))
        A = float(input("c= "))
        Area = 0.5 * a * b * math.sin(A)
        print("Area= ", Area, "\n=================================")
    elif MODE == "3":
        print("-----------------------------------------------------------")
        print("     .    ")
        print("    / \\  ")
        print(" a /   \\ c")
        print("  /     \\")
        print(" /_______\\ ")
        print("     b    ")
        print("formula: Area = ( s * (s - [a]) * ( s - [b]) * ( s - [c]) )^(1/2)")
        a = float(input("a= "))
        b = float(input("b= "))
        c = float(input("c= "))
        s = (a + b + c) * 1/2
        Area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Area= ", Area, "\n=================================")
    elif MODE == "!":
        import area
    else:
        print("\n!!ERROR RESPONSE!!\nPlease Try again\n")
