"""Lesson 2.5: Random"""

__author__ = "Ayaan Adrito"

import random

def roll():
    """Rolls a six sided dice."""
    num = random.randint(1, 6)
    
    print(f"You rolled {num}!")
    
    return num

def rolling_game():
    """Rolling game where you have the roll the same number twice in a row to win."""
    
    tries = 0
    input("Roll your first number: ")
    first_num = roll()
    
    while True:
        input("Roll another number: ")
        second_num = roll()
        tries += 1
        
        if second_num == first_num:
            print(f"You rolled the same number! It took you {tries} tries!")
            break
        else:
            first_num = second_num
            print("Roll again!")

def reverse_number_game():
    MAX_TRIES = 4
    tries = 0
    random_number = int(input("Enter a random number: "))
    guess = 5
    
    while tries < MAX_TRIES:

        hint = input(f"I guess {guess}. Is it correct, higher, or lower?: ")
        tries += 1
        
        if hint == "higher" and tries < 3:
            guess -= 2
        elif hint == "lower" and tries < 3:
            guess += 2
        elif hint == "higher":
            guess -= 1
        elif hint == "lower":
            guess += 1
        else:
            print(f"Yay! I won! The answer is {random_number}!")
            break

def number_game():
    """Runs a number guessing game."""
    
    MAX_TRIES = 3
    MINIMUM = 1
    MAXIMUM = 10
    tries = 0
    random_number = random.randint(MINIMUM, MAXIMUM)
    
    print(f"I'm thinking of a number between {MINIMUM} and {MAXIMUM}.")
    
    while tries < MAX_TRIES:
        guess = int(input("Enter a guess: "))
        
        if guess == random_number:
            print(f"Well done! {random_number} is the correct number!")
            break
        else:
            tries += 1
            hint = ""
            
            if guess > random_number:
                hint = "higher"
            else:
                hint = "lower"
            
            if tries < MAX_TRIES:
                print(f"Wrong! {guess} is {hint} than the correct number... You have {MAX_TRIES - tries} tries left.")
            else:
                print(f"You ran out of tries, you lost! The correct number was {random_number}.")

def main():
    reverse_number_game()

if __name__ == "__main__":
    main()