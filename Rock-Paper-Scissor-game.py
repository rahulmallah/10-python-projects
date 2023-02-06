import random

print("Welcome to the Rock, Paper, Scissors game!")

# list of choices
choices = ["rock", "paper", "scissors"]

# get user choice
user_choice = input("Please choose rock, paper, or scissors: ").lower()

# check if user choice is valid
if user_choice not in choices:
  print("Invalid choice. Please try again.")
  exit()

# get computer choice
computer_choice = random.choice(choices)
print("Computer chose: ", computer_choice)

# determine the winner
if user_choice == computer_choice:
  print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
  print("You won!")
elif user_choice == "paper" and computer_choice == "rock":
  print("You won!")
elif user_choice == "scissors" and computer_choice == "paper":
  print("You won!")
else:
  print("Computer won.")
