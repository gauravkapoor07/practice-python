def division5(n):
    if(n%5 == 0):
        return True 
    return False

a = [1,2,33434,25,353453,255,555,55]

f = list(filter(division5, a))
print(f)