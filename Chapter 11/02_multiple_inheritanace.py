class employee:
    company = "ITC"
    name = "Default Name"
    def show(self):
        print(f"The Name of the employee is: {self.name} and the company is:  {self.company}")

class Coder:
     language = "Python"
     def printLanguage(self):
          print(f"Out of all the languages here is your language: {self.language}")


class Programmer(employee, Coder):  # Derived or Child class is "employee"
    company = "ITC Infotech"
    def showLanguage(self):
          print(f"The namd is {self.company} and he is good with {self.language} language")

a =employee() # OBJECT Created  
b =Programmer()

b.show() #Now only b will run but since the class employee and Coder is parent class in child one then both will also run
b.printLanguage()
b.showLanguage()