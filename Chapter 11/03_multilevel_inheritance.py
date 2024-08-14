class employee:
    a = 1


class Programmer(employee):  # Derived or Child class is "employee"
    b = 2

class Manager(Programmer): # This is a 2nd child class as in manager there is also a 1st child class 
    c = 3                  # named as Programmer also including employee(THE Parent Class) 

o = employee()
print(o.a) # Prints the a attribute
# print(o.b) # shows an error as there is no b attribute in employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)
