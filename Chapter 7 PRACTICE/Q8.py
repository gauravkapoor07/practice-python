'''
For n = 3
*
**
***
'''
n = int(input("Enter the number:"))
for i in range(1, n+1):
  # print(" "* (n-i), end = " ")
  print("*"* (i), end = "")
  print("")
 