import math

print("-----------------------------------------------------------")
print("     A")
print("     .    ")
print("    / \\  ")
print(" b /   \\ ")
print("  /     \\")
print(" /_______\\ ")
print("C    a    B")
print("formula: a = ( [b] * sin[A] )/( sin[B] )")
while True:
    b = float(input("b= "))
    A = float(input("A= "))
    B = float(input("B= "))
    if b <0:
        print("!!ERROR VALUE!!\nValue Should Be Greater Than \'0\'")
    else:
        a = (b * math.sin(A)) / (math.sin(B))
        print("a= ", a, "\n\n")

    back = input("Back to Line?(y/n) :")
    if back == "y":
        import line
