s = {1,5,32,54,5,5,5,"Harry"}
# Sets are unordered and unindexed, and dont contain duplicate values.
print(s, type(s)) 

s.add(566) # To add a element in a set we use setname.add(element to add)
print(s, type(s))

print(len(s))
s.remove(1)
print(s)
