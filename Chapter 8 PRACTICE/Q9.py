def multiply(n):
    for i in range(1, n+1):
        print(f'{n} X {i} = {n*i}')
    return n
n = int(input("Enter the number:"))
print(multiply(n))