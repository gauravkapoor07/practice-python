class employee:
    a = 1
    def __init__(self):
        print("Constructor for employee")


class Programmer(employee):  # Derived or Child class is "employee"
    b = 2
    def __init__(self):
        print("Constructor for Programmer")
        super().__init__()    # This is a SUPER Constructor that is used to use/print the constructor of parent class

class Manager(Programmer): 
    c = 3     
    def __init__(self):
        print("Constructor for Manager")  
        super().__init__()    # This is a SUPER Constructor that is used to use/print the constructor of parent class
                     

# o = employee()
# print(o.a) # Prints the a attribute


# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)