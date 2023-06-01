import math

print("-----------------------------------------------------------")
print("     A")
print("     .    ")
print("    / \\  ")
print(" b /   \\ c")
print("  /     \\")
print(" /_______\\ ")
print("C    a    B")
print("formula: c = ( [a]^2 + [b]^2 - 2*[a]*[b]*cos[C] )^(1/2)")

while True:
    a = float(input("a= "))
    b = float(input("b= "))
    C = float(input("C= "))

    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
    print("c= ", c)

    back = input("Back to Line?(y/n) :")
    if back == "y":
        import line
