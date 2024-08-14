try:
   a = int(input("Hey, Enter a number:"))
   print(a)

except ValueError as v:
      print("Hey")
      print(v)
except Exception as e:
        print(e)

print("Thank You")
# Here program is not crashed or not given any error 
# afterwards code will run as usual