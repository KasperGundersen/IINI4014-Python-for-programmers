"""
    Method that clears a word from punctuation, and makes it lowercase
"""


def pureWord(word):
    punctuation = [",", "\"", ":", ".", "*", "**", "***", "-"]
    for p in punctuation:
        word = word.replace(p, "")

    word = word.lower()
    return word


"""
    The method that finds the frequencies of each word in the given file.
    Takes the filename as the argument.
"""


def getwordfreqs(filename):
    # Opens the given file with read-mode
    with open(file=filename, mode="r") as file:
        # Reads the file
        contents = file.read()

    # Splis the file into word, splits by space
    wordlist = contents.split()

    frequencyDictionary = {}

    # Strips the word before testing if the word is already in the dictionary or not
    for word in wordlist:
        word = pureWord(word=word)

        if (word in frequencyDictionary):
            frequencyDictionary[word] += 1
        else:
            frequencyDictionary[word] = 1

    return frequencyDictionary


"""
    Method thats takes a filename and a word, 
    and returns a list of the lines numbers where the word is found
"""


def getWordsline(filename, searchWord):

    # Cleares the word
    searchWord = pureWord(word=searchWord)

    # Open the file and read each line
    file = open(file=filename, mode="r")

    content = file.readlines()

    linesWithWord = []

    # Turns every line to lowercase and then creates a list of the words in the line
    for number, line in enumerate(iterable=content, start=1):
        line = line.lower()
        words = line.split()

        # If the word is in the line, the line number is saved
        if(searchWord in words):
            linesWithWord.append(number)

    return linesWithWord


"""
    Main method that runs the two functions
"""


def main():
    text = "text.txt"
    word = "word"

    directory = getwordfreqs(filename=text)
    lines = getWordsline(filename=text, searchWord=word)


main()
