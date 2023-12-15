# ITP 115, Fall 2023
# Assignment 3
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825
# Description: Calculator for change in Canadian currency for food items purchased with coins.

#Start by getting food item selection as input
print("Select a food item:\na) Aero Chocolate Bar for $1.95\nb) Beaver Tail Pastry for $7.25\nc) Coffee Crisp for $2.40\nd) Dill Pickle Chips for $4.35")

item = ""
cost = 0

#Branching statement within loop to determine which item the user has chosen and prevent invalid choices.
while cost == 0:
    choice = input("Choice: ").lower()
    if choice == "a":
        item = "Aero Chocolate Bar"
        cost = 195
    elif choice == "b":
        item = "Beaver Tail Pastry"
        cost = 725
    elif choice == "c":
        item = "Coffee Crisp"
        cost = 240
    elif choice == "d":
        item = "Dill Pickle Chips"
        cost = 435
    else:
        print("Invalid selection. Try again.")

#Take inputs for the number of each coin paid and calculate the total payment from that
print("\nPlease enter payment.")
toonies = int(input("# of toonies: "))
loonies = int(input("# of loonies: "))
quarters = int(input("# of quarters: "))
nickels = int(input("# of nickels: "))
payment = 200 * toonies + 100 * loonies + 25 * quarters + 5 * nickels

#Print cost and payment for user
print("\nCost is " + str(cost) + " cents.")
print("Payment it " + str(payment) + " cents.")

#Branching to determine if the user has paid enough for the food item
change = 0
if cost > payment:
    print("\nYou did not pay enough money and will not receive the " + item + ".")
else:
    print("\nYou purchased the " + item + ".")
    change = payment - cost
    print("Change is " + str(change) + " cents.")

    #Calculate and print the number of each type of coin to be returned in change
    changeToonies = change // 200
    print("# of toonies: " + str(changeToonies))
    change = change % 200

    changeLoonies = change // 100
    print("# of loonies: " + str(changeLoonies))
    change = change % 100

    changeQuarters = change // 25
    print("# of quarters: " + str(changeQuarters))
    change = change % 25

    changeNickels = change // 5
    print("# of nickels: " + str(changeNickels))
