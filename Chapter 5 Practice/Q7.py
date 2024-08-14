d1 = {}
# Friend 1 -> Harry
# Friend 2 -> Gaurav
# Friend 3 -> Hardik
# Friend 4 -> Lavesh
print("Welcome User to the Program: ")
print("Harry:")
n1 = input("Enter Your Favourite Language:") 
print("Harry:")
n2 = input("Enter Your Favourite Language:")
print("Hardik:")
n3 = input("Enter Your Favourite Language:")
print("Lavesh:")
n4 = input("Enter Your Favourite Language:")

d1.update({"Harry": n1, "Harry": n2, "Hardik": n3, "Lavesh": n4})
print(d1)
# WHEN NAME ARE SAME THEN BOTH WILL NOT BE PRINTED, THE VALUE WILL BE UPDATED ONCE AGAIN AFTER USING(.update) FUNC.
