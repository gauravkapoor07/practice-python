n = int(input("Enter the number:"))

for i in range(2,n):
    if(n%i) == 0:
        print("No. is not prime")
        break
    else:
        print("No. is prime")
        break