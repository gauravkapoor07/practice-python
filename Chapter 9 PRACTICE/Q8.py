with open("this.txt") as f:
    content = f.read()

contentnew = content

with open("this_copy.txt", "w") as f:
    f.write(contentnew)