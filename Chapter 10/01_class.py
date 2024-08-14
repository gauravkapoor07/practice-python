'''Solving a problem by creating object is one of the most popular approaches in
   programming. This is called object-oriented programming (OOPS).
   This concept focuses on using reusable code (DRY Principle). '''

class employee:
    language = "Py" # Class attribute(LESS PREFERRED THAN INSTANCE ATTRIBUTE)
    salary = 1200000
harry = employee() # This is an object 
harry.name = "Harry"#Instance attribute(MORE PREFERRED)
print(harry.name, harry.language, harry.salary)

rohan = employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to class

# Class is an template
# Memory is only allocated when object is created
'''
Noun → Class → Employee
• Adjective → Attributes → name, age, salary
• Verbs → Methods → getSalary(), increment()
'''