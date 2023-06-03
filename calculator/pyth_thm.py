import math

print("-----------------------------------------------------------")
print(" .")
print(" |\\")
print(" | \\")
print("a|  \\c")
print(" |   \\")
print(" |____\\")
print("   b")
print("formula: [c] = ( [a]^2 + [b]^2 )^(1/2)")
while True:
    print("Put \'0\' in the unknown value you want to find\ne.g.: find [c], then c=0")
    a = float(input("a= "))
    b = float(input("b= "))
    c = float(input("c= "))

    if a == 0:
        a = math.sqrt(c**2 - b**2)
        print("a = ", a, "\n=====================================\n\n")
    elif b == 0:
        b = math.sqrt(c**2 - a**2)
        print("b = ", b, "\n=====================================\n\n")
    elif c == 0:
        c = math.sqrt(a**2 + b**2)
        print("c = ", c, "\n=====================================\n\n")
    else:
        print("!!ERROR INPUT!!")
    back = input("Back to Line?(y/n) :")
    if back == "y":
        import line
