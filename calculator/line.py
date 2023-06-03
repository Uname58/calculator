print("-----------------------------------------------------------")
print(".__________________.")
print("|Line :            |")
print("|__________________|\n")
MODE = 0

while True:
    print("Pythagorean theorem-- 1")  #pyth_thm.py
    print("Rate of Sine--------- 2")  #R_o_S.py
    print("Cosine formula------- 3")  #C_F.py
    print("Back<---------------- !")
    function = input("Choose a function: ")

    if function == "1":
        import pyth_thm
    elif function == "2":
        import R_o_S
    elif function == "3":
        import C_F
    elif function == "!":
        import menu
    else:
        print("\n!!ERROR RESPONSE!!\nPlease Try again\n")
