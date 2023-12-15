# ITP 115, Fall 2023
# Lab 1
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825

def main():

    print("\"Do your little bit of good where you are; it's those little bits of "
          "\ngood put together that overwhelm the world.\""
          "\n- Desmond Tutu")

    name = input("\nEnter your name: ")
    age = int(input("Enter your age: "))
    nextAge = age + 1

    print("\nHello " + name + "!")
    print("Today you are " + str(age) + " years old.")
    print("Next year you will be " + str(nextAge) + " years old.")

main()