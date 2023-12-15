# ITP 115, Fall 2023
# Lab 8
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825

def readFile(userGenre, fileName="lab8_shows.csv"):
    reader = open(fileName, mode="r")
    showList = []
    for line in reader:
        data = line.strip().split(",")
        if data[1] == userGenre:
            showList.append(data[0])
    reader.close()
    return showList

def writeFile(userGenre, showList):
    writer = open(userGenre + ".txt", mode="w")
    for show in showList:
        print(show, file=writer)
    writer.close()

def main():
    genres = ['action', 'animation', 'comedy', 'documentary', 'drama', 'mystery', 'scifi', 'western']
    print("TV Shows")
    print("Possible genres are")
    print(genres)
    userGenre = ""
    while userGenre not in genres:
        userGenre = input("Enter a genre: ").strip().lower()
    writeFile(userGenre, readFile(userGenre))

main()