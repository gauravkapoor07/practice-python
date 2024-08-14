dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2   # Always use( | )
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4} since b id given new value