print("-----------------------------------------------------------")
print(".__________________.")
print("|Area :            |")
print("|__________________|\n")

while True:
    print("Triangle----- 1  | Circle------------ 4")
    print("Square------- 2  | Parallelogram----- 5")
    print("Rectangle---- 3  | Trapezoidal------- 6")
    print("Back--------- !")
    MODE = input("Choose a shape: ")

    if MODE == "1":
        import triangle
    elif MODE == "2":
        import square
    elif MODE == "3":
        import rectangle
    elif MODE == "4":
        import circle
    elif MODE == "5":
        import parallelogram
    elif MODE == "6":
        import trapezoidal
    elif MODE == "!":
        import menu
    else:
        print("\n!!ERROR RESPONSE!!\nPlease Try again\n")
