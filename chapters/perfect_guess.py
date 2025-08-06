''' write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
'''

import random

class GuessTooHigh(Exception):
    pass
class GuessTooLow(Exception):
    pass
class CorrectGuess(Exception):
    pass

def guess(num):
    count=0
    while True:
        n=int(input("enter your guess: "))
        count+=1
        try:
            if n>num:
                raise GuessTooHigh
            elif n<num:
                raise GuessTooLow
            elif n==num:
                raise CorrectGuess
            else:
                print("try again ")
                

        except GuessTooHigh:
            print("Lower number please")   
        except GuessTooLow:
            print("Higher number please")
        except CorrectGuess:
            print(f"correct guess, number of guesses : {count}")
            break
        except ValueError:
            print("invalid guess")

num=random.randint(1,10)

guess(num)
