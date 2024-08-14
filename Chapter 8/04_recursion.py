'''
 factorial(5) = 5 X 4 X 3 X 2 X 1 MATHEMATICAL LOGIC 
 
 factorial(n) = n * factorial(n-1) UNIVERSAL LOGIC OF FACTORIAL
'''

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
n = int(input("Enter the Number:"))
print(f'"The factorial of the number is:", {factorial(n)}')
print("Thank You")