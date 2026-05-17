def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q

print("please  select the operation")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = int(input("Enter your choice"))

a = int(input("Please enter the first number"))
b = int(input("Please enter the second number"))

if choice == 1:
    print(a,"+", b, "=",add (a,b))
if  choice == 2:
    print(a,"-", b, "=",subtract (a,b))
if  choice == 3:
    print(a,"*", b, "=",multiply (a,b))
if  choice == 4:
    print(a,"/", b, "=",divide (a,b))
else:
    print("invalid input")
