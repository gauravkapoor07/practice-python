a = 89 # This is a GLOBAL Variable

def func():
    global a  # This line makes a to a GLOBAL Variable so that we can change its value in func()
    a = 3
    print(a)

func() # Here the value of global a is changed from 89 to 3(the value of a in func())
print(a)
