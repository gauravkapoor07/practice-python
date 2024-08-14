# f = open("file.txt", "r")

# lines =f.readlines() # We have writtern readlines, to print all the lines at once in a LIST
# print(lines, type(lines)) # type becomes list 


# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5 =="")
f = open("file.txt")
line = f.readline()
while(line !=""):
    print(line)
    line = f.readline()
f.close()



