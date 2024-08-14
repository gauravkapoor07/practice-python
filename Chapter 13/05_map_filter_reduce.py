from functools import reduce

# Map Example
l = [1,2,3,4,5]

square = lambda x: x*x # Here it is lambda function

sqlist = map(square, l)
print(list(sqlist))


#Filter Example

def even(n):
    if(n%2==0):
        return True
    else:
        return False
onlyEven  = filter(even,l)
print(list(onlyEven))

# Reduce Function

def sum(a, b):
    return a+b
print(reduce(sum, l)) # It runs on first two nos then it runs on next two nos( First one is the sum result of previous nos) 
                      # and second one is the third(index = 2) no. and it repeats until list is over

      