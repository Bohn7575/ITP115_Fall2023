# ITP 115, Fall 2023
# Assignment 7
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825
# Description: User plays rock-paper-scissors against the computer until one of them wins twice.

import random

# Parameters: none. Return: none. Prints out rules for rock, paper, scissors at beginning of game
def displayRules():
    print("The rules of Rock Paper Scissors are:")
    print("\trock smashes scissors")
    print("\tscissors cut paper")
    print("\tpaper covers rock")
    print("\tIf both hands are the same, it is a tie\n")

# Parameters: hand options. Return: user's hand. Displays hand options and gets user's choice of what to play.
def getUserHand(optionsList):
    print("The options are " + str(optionsList))
    choice = ""
    while choice not in optionsList:
        choice = input("Enter choice: ").strip().lower()
    print("User plays " + choice)
    return choice

# Parameters: hand options. Return: computer's hand. Gets a random choice for computer's hand.
def getComputerHand(optionsList):
    selection = optionsList[random.randint(0,2)]
    print("Computer plays " + selection)
    return selection

# Parameters: user's hand, computer's hand. Return: winner. Uses branching logic to determine who won the game.
def getGameResult(userStr, computerStr):
    result = ""
    if userStr == computerStr:
        result = "tie"
    elif userStr == "rock":
        if computerStr == "paper":
            result = "computer"
        else:
            result = "user"
    elif userStr == "paper":
        if computerStr == "scissors":
            result = "computer"
        else:
            result = "user"
    else:
        if computerStr == "rock":
            result = "computer"
        else:
            result = "user"

    if result == "user":
        print("You win!\n")
    elif result == "computer":
        print("Computer wins.\n")
    else:
        print("You and the computer tied.\n")

    return result

def main():
    options = ["rock", "paper", "scissors"]
    userWins = 0
    computerWins = 0
    displayRules()

    # Loop through game rounds until either user or computer has won twice. Ties do not count for either.
    while userWins < 2 and computerWins < 2:
        user = getUserHand(options)
        computer = getComputerHand(options)
        result = getGameResult(user, computer)
        if result == "user":
            userWins += 1
        elif result == "computer":
            computerWins += 1

    if userWins > computerWins:
        print("You won 2 games!")
    else:
        print("Computer won 2 games.")

main()