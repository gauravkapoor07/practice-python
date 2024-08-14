from typing import List, Union, Tuple, Dict
name: str = "Harry"
# List of integers
numbers: list[int] = [1,2,3,4,5]

# Tuple of a string and a integer
person: Tuple[str, int] = ["Gaurav", 30, 40, "Gaurav"]

# Dictionary with strings keys and integer values 
scores: Dict[str, int] = {"Gaurav": 30, "Bob": 85}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"    # It is used just to make it more compatible 
identifier = 12345 # Also Valid

# These annotations help in making the code self-documenting and allow developers to
# understand the data structures used at a glance.

print(person, name, numbers, scores, identifier)

# n: int = 5

# name: str = "Harry"

# def sum(a,b) -> int:
#     return a+b
# a = sum(3, n)
# print(a) 