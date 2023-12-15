# ITP 115, Fall 2023
# Assignment 2
# Name: First Last
# Email: username@usc.edu
# Section: number or nickname
# Description: (such as)
# This program stores several user inputs, then prints a story using the input values, like a mad-lib.

# Store my name and age
coderName = "Ryan Bohn"
coderAge = 19

# Take user inputs from various categories and store in variables
userName = input("Enter your name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter your favorite food: ")
cost = float(input("Enter cost for food: "))
userAge = int(input("Enter your age: "))

# Variables to store the total cost and age
totalCost = cost * 2
totalAge = coderAge + userAge

# Construct and print story using the above variables and escape characters
print("\nThis code is written by " + coderName + ".")
print("Once upon a time, \"" + userName + "\" and I went to the \"" + place + "\".")
print("We had a yummy lunch eating \"" + food + "\" which cost us $'" + str(totalCost) + "'.")
print("We met a \"" + animal + "\" who made us smile.")
print("We will all be friends for at least '" + str(totalAge) + "' years.")

