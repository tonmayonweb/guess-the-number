#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import win
from art import lose

def check(number,guess_number,guesses):
  if number>guess_number:
    print("Too high")
  elif number<guess_number:
    print("Too low")
  elif number == guess_number:
    print("Good job! you guessed right number")
    print(win)

  
import random
from art import logo
print(logo)
print("I am guessing a number between 1-100 hold tight")
gussed_number = random.randint(1,101)
print(f"pstttt guessed number is {gussed_number}")

guess_left = False
guess_count=0
mode = input("If you are pro then type hard or noob type easy: ")
if mode=="hard":
  guess_count+=5
elif mode=="easy":
  guess_count+=10
while not guess_left:
  user_guess = int(input("Guess a number: "))
  check(user_guess,gussed_number,guess_count)
  guess_count = guess_count-1
  print(f'Number of guess left: {guess_count}')
  if guess_count==0 and user_guess!=gussed_number:
    guess_left=True
    print("Ooops! sorry you ranout of guess ")
    print(lose)
  elif user_guess==gussed_number:
    guess_left=True
    








