class employee:
    company = "ITC"
    def show(self):
        print(f"The Name of the employee is {self.name} and the salary is {self.salary}")


#class Programmer:
#        company = "ITC Infotech"
#        def show(self):   
 #        print(f"The Name is {self.name} and the salary is {self.salary}")
#        def showLanguage(self):
#            print(f"The namd is {self.name} and he is good with {self.language} language")


class Programmer(employee):  # Derived or Child class is "employee"
    company = "ITC Infotech"
    def showLanguage(self):
          print(f"The namd is {self.name} and he is good with {self.language} language")

a =employee() # OBJECT Created  
b =Programmer()
print(a.company, b.company)