from functools import reduce
a = [1,2,44,25,33,55,555,55,635]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater, a))

