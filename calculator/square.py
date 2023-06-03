
while True:
    print("Basic    Formula<---- 1")
    print("Diagonal Formula<---- 2")
    print("Back To Area<-------- !")
    MODE = input("Mode<---- ")

    if MODE == "1":
        print("-----------------------------------------------------------")
        print("  .__________.")
        print("  |          |")
        print("l |          |")
        print("  |          |")
        print("  |__________|")
        print("formula: Area = [l]^2")
        l = float(input("l= "))
        A = l ** 2
        print("Area= ", A, "\n")
    elif MODE == "2":
        print("-----------------------------------------------------------")
        print(".______.")
        print("|    / |")
        print("| d/   |")
        print("|/_____|")
        print("formula: Area = ( [d]^2 )/2")
        d = float(input("d= "))
        Area = (d ** 2)/2
        print("Area= ", Area, "\n")
    elif MODE == "!":
        import area
    else:
        print("\n!!ERROR RESPONSE!!\nPlease Try again\n")
