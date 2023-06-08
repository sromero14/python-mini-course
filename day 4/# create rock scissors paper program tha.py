# create rock scissors paper program that asks for user input
# 0 = rock 1 = scissors 2 = paper

import random

def whatIsIt(num):
  if num < 0 or num > 2: 
    return "You gave a wrong number! Number has to be between 0 and 2"
  choices = ["Rock", "Scissors", "Paper"]
  return choices[num]

#gives back 0-2 at random
def computerChoice():
  return random.randint(0, 2)

def rockScissorsPaper():
  #Code here
  #ask user for a choice of rock scissor paper
  user_choice = input("Choose rock or scissors or paper: ")
  print(user_choice)

  # if statement that checks if user's user_choice is correct
  if user_choice == "Rock" or user_choice == "Scissors" or user_choice == "Paper":
    print("Your respose is valid")
  else:
    print("Your respose is not valid")
  
  #computer choice
  computer_choice = whatIsIt(computerChoice())
  print("computer choice: ")
  print(computer_choice)

  # print tie if user and computer respose is the same
  if user_choice == computer_choice:
    print("It's a tie!")
  else: 
    if user_choice == "Rock":
      if computer_choice == "Scissors":
        print("The user won!")
      if computer_choice == "Paper":
        print("The computer won!")
    elif user_choice == "Scissors":
      if computer_choice == "Paper":
        print("The user won!")
      if computer_choice == "Rock":
        print("The computer won!")
    elif user_choice == "Paper":
      if computer_choice == "Rock":
        print("THe user won!")
      if computer_choice == "Scissors":
        print("The computer won!")


  #print random computer response
  # print(whatIsIt(computerChoice()))

rockScissorsPaper()

# create rock scissors paper program that asks for user input
# 0 = rock 1 = scissors 2 = paper

import random

def whatIsIt(num):
  if num < 0 or num > 2: 
    return "You gave a wrong number! Number has to be between 0 and 2"
  choices = ["Rock", "Scissors", "Paper"]
  return choices[num]

#gives back 0-2 at random
def computerChoice():
  return random.randint(0, 2)

def rockScissorsPaper():
  #Code here
  #ask user for a choice of rock scissor paper
  user_choice = input("Choose rock or scissors or paper: ")
  print(user_choice)

  # if statement that checks if user's user_choice is correct
  if user_choice == "Rock" or user_choice == "Scissors" or user_choice == "Paper":
    print("Your respose is valid")
  else:
    print("Your respose is not valid")
  
  #computer choice
  computer_choice = whatIsIt(computerChoice())
  print("computer choice: ")
  print(computer_choice)

  # print tie if user and computer respose is the same
  if user_choice == computer_choice:
    print("It's a tie!")
  else: 
    if user_choice == "Rock":
      if computer_choice == "Scissors":
        print("The user won!")
      if computer_choice == "Paper":
        print("The computer won!")
    elif user_choice == "Scissors":
      if computer_choice == "Paper":
        print("The user won!")
      if computer_choice == "Rock":
        print("The computer won!")
    elif user_choice == "Paper":
      if computer_choice == "Rock":
        print("THe user won!")
      if computer_choice == "Scissors":
        print("The computer won!")


  #print random computer response
  # print(whatIsIt(computerChoice()))

rockScissorsPaper()

