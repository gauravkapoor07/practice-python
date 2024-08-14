class Employee:
    a = 1
    @classmethod        # It is a method used to show the class attribute and not instance attribute
    def show(cls):
        print(f"The class value of a is {cls.a}") # cls is just a symbol used to show neat and clean code
e = Employee()
e.a = 45
e.show()