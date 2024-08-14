letter = ''' Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>","Gaurav").replace("<|Date|>","5th july, 2024")) 
# Here we used .replace() Function to replace the name and date, to fill it with appropriate characters.
