import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    guesses +=1
    a = int(input("Guess a number:"))
    if(a>n):
        print("Enter a lower no.")
        pass
    elif(a<n):
        print("Enter a higher no.")
        pass
    elif(a==n):
       print("Your guess is correct!")
       print("You WON!")
    else:
       print("Invalid Input")
       print("Thank You for playing!")
       break
print(f"You guessed the correct no. in {guesses} attempts.")