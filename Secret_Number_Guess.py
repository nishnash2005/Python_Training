# This is a User_Guess the Ran_Number game.
import random

User_Entry = 0

print('Hello! What is your name?')
User_Name = input()

Ran_Number = random.randint(0, 100)
print('Hello, ' + User_Name + ', I am thinking of a number between 0 and 100.')

while User_Entry < 11:
    print('Lets guess the number:') # There are four spaces in front of print.
    User_Guess = input()
    User_Guess = int(User_Guess)

    User_Entry = User_Entry + 1

    if User_Guess < Ran_Number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if User_Guess > Ran_Number:
        print('Your guess is too high.')

    if User_Guess == Ran_Number:
        break

if User_Guess == Ran_Number:
    User_Entry = str(User_Entry)
    User_Guess = str(User_Guess)
    print('Good job, ' + User_Name + '! You guessed my number ' + User_Guess + ' in ' + User_Entry + ' guesses!')

if User_Guess != Ran_Number:
    Ran_Number = str(Ran_Number)
    print('Nope. The number I was thinking of was ' + Ran_Number)