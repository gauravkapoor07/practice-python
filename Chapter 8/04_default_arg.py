def goodDay(name, ending = "thank you"):  # here Ending is a DEFAULT PARAMETER and can be overidden by giving input 
    print("Hello, ", name)
    print(ending)
goodDay("Harry") # Here ending will be printed as default
goodDay("Harry", "Thanks") # here "thanks" will be printed rather than "thank you"