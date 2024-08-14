a = 5 #<class 'int'>
b = "5" # <class 'str'>  Double coat means string even it contain nos.

t = type(a)
T = type(b)


c = int(b) # data type is changed of b from string literal to integer and it shows when printed
Y = type(c)

print(t)
print(T)
print(Y)