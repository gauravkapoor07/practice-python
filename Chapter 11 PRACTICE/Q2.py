class Animals:
    pass

class Pets(Animals):
    pass
        

class Dog(Pets):
    
     @staticmethod  # This is used to not to use self here.
     def bark():
         print("Bow Bow!")
         
    


# a = Animals()
# p = Pets()
d = Dog()
Dog.bark()
