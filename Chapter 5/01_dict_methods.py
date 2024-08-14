emptydic = {} # Always use {} in dictionary

marks = {
    "Harry": 100,
    "Shubham":56,
    "Rohan":23
}
print(marks, type(marks))

# Dictionary start with {}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry":99, "Renuka":26}) # Adds or change the value 
print(marks)
print(marks.get("Renuka")) # Gives the value at the key entered
print(len(marks))
