""" Guessing Game Challenge
Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. 
The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly 
and how many guesses it took! """

# First, pick a random integer from 1 to 100 using the random module and assign it to a variable
# Note: random.randint(a,b) returns a random integer in range [a, b], including both end points.

import random

number = random.randint(1,100)

#Next, print an introduction to the game and explain the rules

print("Guess the correct number between 1 and 100")

#Create a list to store guesses
#Hint: zero is a good placeholder value. It's useful because it evaluates to "False"

empty = 0

#Write a while loop that asks for a valid guess. Test it a few times to make sure it works.

while True:
    guess = int(input("Enter your guess: "))
    if empty == 0:
        print("Out of Bounds")
    elif empty == range(1,10):
        print() 


# Method 1

import random

def guess_game():
    
    """
    This function implements a number guessing game. The computer picks a random integer between 1 and 100, and the player
    has to guess the number by entering their guesses. The rules of the game are as follows:
    - If the player's guess is less than 1 or greater than 100, the program will say 'OUT OF BOUNDS'.
    - On the player's first turn, if their guess is within 10 of the number, the program will say 'WARM!'.
    - If their guess is further than 10 away from the number, the program will say 'COLD!'.
    - On all subsequent turns, if the player's guess is closer to the number than the previous guess, the program will say 'WARMER!'.
    - If the player's guess is farther from the number than the previous guess, the program will say 'COLDER!'.
    - The game continues until the player correctly guesses the number, at which point the program will say how many guesses
    it took.
    """
    
    num = random.randint(1,100)
    guesses = [0]
    while True:
        guess = int(input("Enter your guess: "))
        if guess < 1 or guess > 100:
            print("OUT OF BOUNDS")
        elif abs(num - guess) <= 10:
            if guesses[-1] == 0:
                print("WARM!")
            else:
                print("WARMER!")
        else:
            if guesses[-1] == 0:
                print("COLD!")
            else:
                print("COLDER!")
        if guess == num:
            print(f"You've guessed correctly! It took you {len(guesses)} guesses.")
            break
        guesses.append(guess)

guess_game()

#Method 2

import random

def guess_game():
    
    """
    This function implements a number guessing game. The computer picks a random integer between 1 and 100, and the player
    has to guess the number by entering their guesses. The rules of the game are as follows:
    - If the player's guess is less than 1 or greater than 100, the program will say 'OUT OF BOUNDS'.
    - On the player's first turn, if their guess is within 10 of the number, the program will say 'WARM!'.
    - If their guess is further than 10 away from the number, the program will say 'COLD!'.
    - On all subsequent turns, if the player's guess is closer to the number than the previous guess, the program will say 'WARMER!'.
    - If the player's guess is farther from the number than the previous guess, the program will say 'COLDER!'.
    - The game continues until the player correctly guesses the number, at which point the program will say how many guesses
    it took.
    """
    
    num = random.randint(1,100)
    guess = int(input("Enter your guess: "))
    guesses = 1

    while guess != num:
        if guess < 1 or guess > 100:
            print("OUT OF BOUNDS")
        elif guesses == 1:
            if abs(num - guess) <= 10:
                print("WARM!")
            else:
                print("COLD!")
        else:
            if abs(num - guess) < abs(num - prev_guess):
                print("WARMER!")
            else:
                print("COLDER!")
        prev_guess = guess
        guess = int(input("Enter your guess: "))
        guesses += 1

    print(f"You've guessed correctly! It took you {guesses} guesses.")

guess_game()