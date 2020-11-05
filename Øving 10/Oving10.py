# Function that returns the words from a text in a dictionary
# with the word as the key and the occurrence as the value
def getwordfreqs(filename):
    import re
    # Opens the given file with read-mode
    with open(file=filename, mode="r") as file:
        # Reads the file
        content = file.read()
    # Splis the file into word, splits by space and punctuations
    wordList = re.split(
        "(?:(?:[^a-zA-Z]+')|(?:'[^a-zA-Z]+))|(?:[^a-zA-Z']+)", content)
    wordFrequency = {}

    # Strips the word before testing if the word is already in the dictionary or not
    for word in wordList:
        cleanWord = word.lower().strip()

        if (cleanWord in wordFrequency):
            wordFrequency[cleanWord] += 1
        else:
            wordFrequency[cleanWord] = 1

    return wordFrequency

# 1. Sentence length in words
# Function that returns the length of sentences by words in a text
def sentenceLength(filename):
    import re
    with open(file=filename, mode="r") as file:
        content = file.read()

    # Splits the text into sentences
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', content)
    sentenceDictionary = {}

    # Counts the amount of words in each sentence
    for number, sentence in enumerate(iterable=sentences, start=1):
        sentenceDictionary[number] = len(sentence.split())

    return sentenceDictionary

# 2. Percentage of easy words: easy words are those used frequently: they have high frequency in documents,
# 3. Percentage of difficult words: difficult words are those that are seldom used and have low frequency in documents,

# Function that return easy and difficult words in a text
def wordDifficulty(dictionary):
    easyWords = []
    difficultWords = []

    # a word is difficult if it only used onw time in the text and easy if it i used more than 30 times
    for word in dictionary:
        if(dictionary[word] == 1):
            difficultWords.append(word)
        if(dictionary[word] > 30):
            easyWords.append(word)

    return easyWords, difficultWords

# 4. Percentage of different words: A count of the unique words in the document divide by the total number of words,
# Function that returns the percentage of different words
def wordPercentage(dictionary):
    uniqueWords = len(dictionary)
    amtWords = sum(dictionary.values())

    return (uniqueWords/amtWords)*100

# 5. Number of sentences per paragraph.
# Function that counts sentences per paragraph in a text
def sentencesPerParagraph(filename):
    import re
    with open(file=filename, mode="r") as file:
        content = file.read()

    # Concider text a paragraph if it got two new lines in a row
    paragraphs = content.split('\n\n')
    sentencesDictionary = {}

    # Splits the paragraphs into sentences, and count how many sentences per paragraph
    for number, paragraph in enumerate(iterable=paragraphs, start=1):
        sentences = re.split(r' *[\.\?!][\'"\)\]]* *', paragraph)
        sentencesDictionary[number] = len(sentences)

    return sentencesDictionary


def main():
    text = "text.txt"

    wordFrequency = getwordfreqs(filename=text)
    sentences = sentenceLength(filename=text)
    paragraphs = sentencesPerParagraph(filename=text)
    easyWords, difficultWords = wordDifficulty(dictionary=wordFrequency)
    percentage = wordPercentage(dictionary=wordFrequency)


main()
