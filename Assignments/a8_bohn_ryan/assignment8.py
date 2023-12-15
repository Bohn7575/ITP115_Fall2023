# ITP 115, Fall 2023
# Assignment 8
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825
# Description: Simulates crack the code game by generating a random list of numbers and giving the user hints until they accuratey guess the code.

import random

# Parameter: a string of user input. Return: boolean indicating if string is a single digit.
def isSingleDigit(userStr):
    if len(userStr) == 1:
        if userStr.isdigit():
            return True
    return False

# Parameter: number of digits to generate. Return: list of random integers 0-9
def createCodeList(num):
    code = []
    for i in range(num):
        code.append(random.randint(0, 9))
    return code

# Parameter: number of digits to get. Return: list of guesses inputted by the user.
# Gets user input of digits to guess the code.
def createUserList(num):
    print("The number of digits in the code is " + str(num))
    guess = []
    for i in range(num):
        entry = input("Enter a digit at index " + str(i) + ": ")
        while not isSingleDigit(entry):
            entry = input("Enter a digit at index " + str(i) + ": ")
        guess.append(int(entry))
    print("Your guess is " + str(guess) + "\n")
    return guess

# Parameters: list of code digits, list of user guesses, and number of values in the lists. Return: none.
# Tells the user any guesses that are correct and in the right spot, as well as any guesses in the wrong spot and how many there are.
def displayHints(codeList, userList, num):
    print("Generating hints...")
    hintsGiven = False
    for i in range(num):
        if userList[i] == codeList[i]:
            print("index " + str(i) + " -> " + str(userList[i]) + " is correct")
            hintsGiven = True
        if userList[i] in codeList:
            print("index " + str(i) + " -> " + str(userList[i]) + " occurs " + str(codeList.count(userList[i])) + " time(s)")
            hintsGiven = True
    if not hintsGiven:
        print("No correct digits")
    print()

# Main method to run the game. Tracks how many times the user has made a guess and continues until user guesses correctly. Displays number of guesses when finished.
def main():
    numDigits = 3
    codeList = createCodeList(numDigits)
    userList = createUserList(numDigits)
    count = 1
    while not userList == codeList:
        displayHints(codeList, userList, numDigits)
        userList = createUserList(numDigits)
        count += 1
    print("You cracked the code in " + str(count) + " guesses!")

main()