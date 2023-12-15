# ITP 115, Fall 2023
# Assignment 9
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825
# Description: Create files with information on programming languages with a field chosen by the user

# Reads the top line of languages.csv to create a list of data fields for the user to choose from
# Parameters: file to read from
# Return: list of data field options
def createChoiceList(fileStr="languages.csv"):
    reader = open(fileStr, mode="r")
    header = reader.readline().strip()
    reader.close()
    return header.split(sep=",")

# Reads the requested field from each entry in the languages.csv file to produce a list of values
# Parameters: list of possible fields, field chosen by the user, and file to read from
# Return: list of values in that field for every csv entry
def createInfoList(choiceList, choiceStr, fileStr="languages.csv"):
    returnList = []
    index = choiceList.index(choiceStr)
    reader = open(fileStr, mode="r")
    reader.readline()
    for line in reader:
        lineList = line.strip().split(",")
        returnList.append(lineList[index])
    reader.close()
    return returnList

# Prompts the user to input the data field they want to create a file for from the possible options, excluding id and title
# Parameters: list of possible fields to chose from
# Return: user's chosen field
def getUserChoice(choiceList):
    slicedChoices = choiceList[2:]
    print("Available information about the languages includes")
    print(slicedChoices)
    choice = input("Enter your choice: ").strip().lower()
    while choice not in slicedChoices:
        print(choice + " is not a valid choice.")
        choice = input("Enter your choice: ").strip().lower()
    print("You have entered " + choice + ".")
    return choice

# Creates a text file named according to the users choice that contains pairs of names and values in the chosen category
# Parmaters: list of language titles, list of requested info, choice of info type
# Return: none
def writeFile(langList, infoList, choiceStr):
    writer = open(choiceStr + ".txt", mode="w")
    print("language -> " + choiceStr, file=writer)
    for i in range(len(langList)):
        if not infoList[i] == "NA":
            print(langList[i] + " -> " + infoList[i], file=writer)
    writer.close()

def main():
    print("Computer Languages")
    choiceList = createChoiceList()
    langList = createInfoList(choiceList, "title")
    userChoice = getUserChoice(choiceList)
    infoList = createInfoList(choiceList, userChoice)
    writeFile(langList, infoList, userChoice)

main()