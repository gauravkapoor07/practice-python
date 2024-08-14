def sumofnaturalnos(n):
    sum = n/2 * (n+1)
    return sum
n = int(input("Enter the number:"))
print(sumofnaturalnos(n))


# OR it can be written as

# def sum(n):
#     if(n==1):
 #        return 1
 #    return sum(n-1) + n

# print(sum(4))