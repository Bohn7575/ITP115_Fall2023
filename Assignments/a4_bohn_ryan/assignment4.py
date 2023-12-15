# ITP 115, Fall 2023
# Assignment 4
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825
# Description: Takes in 2 lists of numbers, determines the max of the first and min of the second

def main():

    # Initialize count and total variables, prompt user, and get starting value for max
    count = 0
    total = 0
    print("Find the largest number\nEnter an integer (negative # to quit)")
    current = int(input("> "))
    max = current

    # Loop until user quits with negative number, increasing total, count, and setting max when necessary
    while current >= 0:
        if current > max:
            max = current
        total += current
        count += 1
        current = int(input("> "))

    # If the user entered numbers in the list, calculate average and print results to user
    if max >= 0:
        average = total / count

        print("The largest number is " + str(max))
        print("The count is " + str(count))
        print("The total is " + str(total))
        print("The average is " + str(average))

    # Initialize count and total variables, prompt user, and get starting value for min
    count = 0
    total = 0
    print("\nFind the smallest number\nEnter an integer (negative # to quit)")
    current = int(input("> "))
    min = current

    # Loop until user quits with negative number, increasing total, count, and setting min when necessary
    while current >= 0:
        if current < min:
            min = current
        total += current
        count += 1
        current = int(input("> "))

    # If the user entered numbers in the list, calculate average and print results to user
    if min >= 0:
        average = total / count

        print("The smallest number is " + str(min))
        print("The count is " + str(count))
        print("The total is " + str(total))
        print("The average is " + str(average))

main()
# This is painful without functions