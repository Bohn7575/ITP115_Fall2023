# ITP 115, Fall 2023
# Lab 4
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825

def main():

    phrase = input("Enter a phrase: ")
    changes = 0
    print("Your new passphrase is")

    for ch in phrase:
        if ch in "AEIiST1":
            changes += 1
            if ch == "A":
                print(4, end = "")
            elif ch == "E":
                print(3, end = "")
            elif ch == "I" or ch == "i":
                print(1, end = "")
            elif ch == "S":
                print("$", end = "")
            elif ch == "T":
                print(7, end = "")
            else:
                print("!", end = "")
        else:
            print(ch, end = "")

    print("\nChanged " + str(changes) + " characters")

main()