class employee:
    language = "Python" # Class attributes is less peferred 
    salary = 1200000

    def getInfo(self):# Self attributes
       print(f"The Language is {self.language}. The salary is {self.salary}")

    def greet(self): # Self should be given to the function
       print("Good Morning")
    
    
    @staticmethod   #DECORATOR
    def greet(): # If you dont want to use self then use decorator @staticmethod
       print("Good Morning")


harry = employee()
# harry.language = "Javascript"#Instance attribute is given more preference than class attribute
harry.getInfo() # SAME as employee.getinfo(harry)
harry.greet()
# employee.getinfo(harry) SAME as Above Command
# self refers to the instance of the class. It is automatically passed with a function call from an object.