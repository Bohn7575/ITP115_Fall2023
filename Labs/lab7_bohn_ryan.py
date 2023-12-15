# ITP 115, Fall 2023
# Lab 7
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825

import random

def getUserOption(optionsList):
    choices = " or ".join(optionsList)
    userInput = ""
    while userInput not in optionsList:
        userInput = input("Enter " + choices + ": ").strip().lower()
    print("User entered " + userInput)
    return userInput

def getRandomOption(optionsList):
    computerChoice = random.choice(optionsList)
    print("Computer selected " + computerChoice)
    return computerChoice

def main():
    options = ["heads", "tails"]
    user = getUserOption(options)
    computer = getRandomOption(options)
    if user == computer:
        print("You matched!")
    else:
        print("No match.")

main()