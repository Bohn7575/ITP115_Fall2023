# ITP 115, Fall 2023
# Lab 9
# Name: Ryan Bohn
# Email: rbohn@usc.edu
# Section: 31825

def readFile(fileName):
    words = {}
    reader = open(fileName, mode="r")
    for line in reader:
        for word in line.strip().split():
            word = word.strip(",.?:;").lower()
            if not word in words:
                words[word] = 1
            else:
                words[word] += 1
    reader.close()
    return words

def sortKeys(dictionary):
    keys = list(dictionary.keys())
    keys.sort()
    return keys


def main():
    poemDict = readFile("lab9_poem.txt")
    sortedPoemWords = sortKeys(poemDict)
    print("Words and their number of occurrences:")
    for word in sortedPoemWords:
        print(word + " -> " + str(poemDict[word]))

main()