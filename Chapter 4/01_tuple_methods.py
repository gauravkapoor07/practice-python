# Tuple is a type of IMMUTABLE data type in python.
# Tuple always start with ()

a = (1,2,2,5,6)
print(type(a))
b = (1) # after inserting a comma it shows that data type is a tuple
print(type(b))

no = a.count(2) # Tells the no. of times the value is repeated
print(no)
i = a.index(5) # Tells the index of the entered value
print(i)
