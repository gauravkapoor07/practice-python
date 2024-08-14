words = ["donkey", "bad", "ganda"]

with open("donkeyfile.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("donkeyfile.txt", "w") as f:
    f.write(content)