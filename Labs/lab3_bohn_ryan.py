# ITP 115, Fall 2023
# Lab 3
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825

print("Get to know my favorite people...\nA) Artist\nB) Athlete\nC) Author\nQ) Quit")
choice = input("Option: ").lower()
numMessages = 0
while choice != "q":
    if choice == "a":
        print("My favorite artist is J. Cole.")
    elif choice == "b":
        print("My favorite athlete is Aaron Donald.")
    elif choice == "c":
        print("My favorite author is Agatha Christie.")
    else:
        print("That is not a valid choice.")
    numMessages+=1
    choice = input("Option: ").lower()

if numMessages > 0:
    print("You got " + str(numMessages) + " messages.")