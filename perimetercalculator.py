def pers(p):
    return p * 4
def perr(p,q):
    return 2*p + 2*q

print("please select operation")
print("1.perimeter of square")
print("2.perimeter of rectangle")

choice = int(input("please enter your choice"))

l = int("Enter length")
b = int("enter breadth")

if choice == 1:
    print("Perimeter of square = ",pers(l))
if choice == 2:
    print("Perimeter of rectangle = ",perr(l,b))
else:
    print("invalid")

