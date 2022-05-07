import random

print("Hello! What is your name?")
username = input()

print(username +" ,tell me the range of numbers to think from")
low = int(input("the minimum is: "))
high = int(input("the maximum is: "))

SecretNumber = random.randint(low,high)

print(username + ",Now I am thinking of a number between " +
        str(low) + " and " + str(high)+"\n can you guess it?")

print("Remember, you have only 5 attempt")
guessCounter = 0
for guessCounter in range(1, 9):
    print("take guess :")
    guess = int(input())

    if guess < SecretNumber:
        print("Your guess is too low.")

    elif guess > SecretNumber:
        print('Your guess is too high.')
        
    else: break   
    
if guess == SecretNumber:
    print("Good job, "+ username + "! You guessed my number in " +
          str(guessCounter)+ " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(SecretNumber))
    