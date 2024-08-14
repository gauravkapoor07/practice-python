word = "donkey"
with open("donkeyfile.txt", "r") as f:
    content = f.read()

contentnew = content.replace(word, "#####")

with open("donkeyfile.txt", "w") as f:
    f.write(contentnew)