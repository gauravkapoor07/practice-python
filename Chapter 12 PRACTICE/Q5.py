n = int(input("Enter the number:"))

table = [n*i for i in range(1,11)]
with open("multiplicationtableQ3ch12.txt", "w") as f:
     f.write(f"Table of {n}: {str(table)} \n")