def greatest(a, b, c):
    if (a>b and a>c):
        print("a is Greatest")
    elif(b>c and b>a):
        print("b is the Greatest")
    elif(c>a and c>b):
        print("c is the Greatest")
    elif(a ==b or a == c ):
     print("ALL ARE THE GREATEST")

a = int(input("Enter the number a:"))
b = int(input("Enter the number b:"))
c = int(input("Enter the number c:"))
greatest(a , b , c)
