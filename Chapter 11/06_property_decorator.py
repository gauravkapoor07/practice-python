class Employee:
    a = 1
    @classmethod        # It is a method used to show the class attribute and not instance attribute
    def show(cls):
        print(f"The class value of a is {cls.a}") # cls is just a symbol used to show neat and clean code
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]  # Split divide the string into parts and make a list
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45
e.name = "Gaurav Kapoor"
print(e.fname, e.lname)

e.show()