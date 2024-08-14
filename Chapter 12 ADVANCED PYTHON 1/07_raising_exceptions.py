a = int(input("Enter a Number:"))
b = int(input("Enter second Number:"))

if(b == 0):
    raise ZeroDivisionError("Hey, Our program is not meant to divide number by zero")
else:
    print("The division of Number 1 and Number 2 is:", a/b)