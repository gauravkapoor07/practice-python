class employee:
    language = "Py" # Class attributes is less peferred 
    salary = 1200000
harry = employee()
harry.language = "Javascript"#Instance attribute is given more preference than class attribute
print( harry.language, harry.salary)

# When looking up for harry.attribute it checks for the following:
# 1) Is attribute present in object?
# 2) Is attribute present in class?

# Here name is instance attribute and salary and language are class attributes as they directly belong to class
