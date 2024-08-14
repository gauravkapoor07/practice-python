class employee:
    name = "harry"
    language = "Python" # Class attributes is less peferred 
    salary = 1200000

    def __init__(self, name , salary, language):  # dunder method which is automatically called
       self.name = name
       self.salary = salary
       self.language = language 
       print("I am Creating an object")
    
    # def getInfo(self):# Self attributes
    #    print(f"The Language is {self.language}. The salary is {self.salary}")

    # def greet(self): # Self should be given to the function
     #   print("Good Morning")
    
    
    @staticmethod   #DECORATOR
    def greet(): # If you dont want to use self then use decorator @staticmethod
       print("Good Morning")


harry = employee( "Gaurav", 1300000, "Javascript")
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)