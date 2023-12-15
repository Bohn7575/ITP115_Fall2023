# ITP 115, Fall 2023
# Lab 2
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825

year = input("Enter year: ")

zodiac = int(year) % 12

if zodiac == 0 :
    animal = "Monkey"
elif zodiac == 1 :
    animal = "Rooster"
elif zodiac == 2 :
    animal = "Dog"
elif zodiac == 3 :
    animal = "Pig"
elif zodiac == 4 :
    animal = "Rat"
elif zodiac == 5 :
    animal = "Ox"
elif zodiac == 6 :
    animal = "Tiger"
elif zodiac == 7 :
    animal = "Rabbit"
elif zodiac == 8 :
    animal = "Dragon"
elif zodiac == 9 :
    animal = "Snake"
elif zodiac == 10 :
    animal = "Horse"
else:
    animal = "Goat"

print(year + " is the year of the " + animal)