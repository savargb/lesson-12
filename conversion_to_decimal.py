def bin(n):
    if n == 0:
        return "0"
    
    binstr == ""
    while n>0:
        remainder = n%2
        binstr = str(remainder) + binstr
        n = n/2
    
    return binstr

def octal(n):
    if n == 0:
        return "0"

    octalstr == ""
    while n>0:
        remainder = n%8
        octalstr = str(remainder) + octalstr
        n = n/8
    
    return octalstr

def hexad(n):
    if n == 0:
        return "0"

    hexadstr == ""
    while n>0:
        remainder = n%8
        hexadstr = str(remainder) + hexadstr
        n = n/8
    
    return hexadstr

print("Selcet option: ")
print("1. Binary to Decimal")
print("2. Octal to Decimal")
print("3. Hexadecimal to Decimal")

choice = int(input("Enter the choice"))

n = int(input("Enter the number"))

if choice == 1:
    print("Binary to decimal is:", bin(n))
elif choice == 2:
    print("Octal to decimal is:", octal(n))
elif choice == 3:
    print("Hexadecimal to decimal is:", hexad(n))
else:
    print("Invalid")



