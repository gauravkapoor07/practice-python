try:
   a = int(input("Hey, Enter a number:"))
   print(a)


except Exception as e:
        print(e)

else: # else will only run if try is executed successfully
      print("I am Inside Else")

