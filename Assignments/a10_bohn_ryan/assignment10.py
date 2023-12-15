# ITP 115, Fall 2023
# Assignment 10
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825
# Description: Allow user to add to modify and read a dictionary of calendar events and their date.

# Print all stored events and their dates to the user
# Parameters: events dictionary
# Return: none
def displayEvents(eventDict):
    eventNames = list(eventDict.keys())
    eventNames.sort()
    for event in eventNames:
        print(event + " occurs on " + eventDict[event])

# Allow user to add a new event to the dictionary and enter its date
# Parameters: events dictionary
# Return: none
def addEvent(eventDict):
    eventName = input("Enter an event: ").title()
    if eventName in eventDict:
        print(eventName + " is already in the events dictionary.")
    else:
        eventDate = input("Enter the date: ").title()
        eventDict[eventName] = eventDate
        print(eventName + " has been added to the events dictionary.")

# Change the date of an event that is already in tbe dictionary
# Parameters: events dictionary
# Return: none
def updateEvent(eventDict):
    eventName = input("Enter an event: ").title()
    if eventName not in eventDict:
        print(eventName + " is not in the events dictionary.")
    else:
        eventDate = input("Enter the date: ").title()
        eventDict[eventName] = eventDate
        print(eventName + " has been updated to " + eventDate + ".")

# Delete a user-specified event from the dictionary
# Parameters: events dictionary
# Return: none
def deleteEvent(eventDict):
    eventName = input("Enter an event: ").title()
    if eventName not in eventDict:
        print(eventName + " is not in the events dictionary.")
    else:
        del eventDict[eventName]
        print(eventName + " was deleted from the events dictionary.")

# Main function
def main():
    events = {"Christmas" : "December 25", "Halloween" : "October 30"}
    displayEvents(events)
    choice = ""
    while choice != "q":
        print("\nEvents Dictionary\n" +
              "A) Add an event\n" +
              "U) Update an event\n" +
              "D) Delete an event\n" +
              "P) Print the events\n" +
              "Q) Quit")
        choice = input("Choice: ").lower()
        if choice == "a":
            addEvent(events)
        elif choice == "u":
            updateEvent(events)
        elif choice == "d":
            deleteEvent(events)
        elif choice == "p":
            displayEvents(events)
        elif choice != "q":
            print("Invalid choice.")

main()