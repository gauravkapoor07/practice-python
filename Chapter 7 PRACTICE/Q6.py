# 5! = 1X2X3X4X5

n  = int(input("Enter the Number you want the FACTORIAL:"))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"the Factorial of {n} is {product}")