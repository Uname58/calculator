while True:
    print("-----------------------------------------------------------")
    print(".__________________.")
    print("|Menu :            |")
    print("|__________________|\n")
    ''''line.py'''
    print("Line ----------------1")
    print("=====================================")
    '''area.py'''
    print("Area ----------------2")
    print("=====================================")
    '''volume.py'''
    print("Volume --------------3")
    print("=====================================")
    '''other.py'''
    print("Other ---------------4")
    print("=====================================")
    MODE = input("Choose a Mode\n>>>>")

    if MODE == "1":
        import line
    elif MODE == "2":
        import area
