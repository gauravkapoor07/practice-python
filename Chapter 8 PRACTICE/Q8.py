def remove(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n 
l = ["Harry", "Rohan", "Shubham", "an"]

print(remove(l, "an"))