# in the example, the textfile contains:
# a aa c AA BBBBBBB cc b bb dd c

# A method that opens a file and puts every word into a list
def fillList(filename):

    # The with statement automatically takes care of closing the file
    # once it leaves the with block, even in cases of error.
    with open(filename, "r") as file:
        strings = file.read().split()

    # Returns the list of words in lowercase
    return [word.lower() for word in strings]

# This is a insertion Sort, that sorts the length of the words


def sortLength(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and len(alist[position-1]) > len(currentvalue):
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

# This is a selction sort, that sorts the word alphabetically


def sortAlphabetically(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


# The main methods creates a list of strings
# Then sort the list alphabetically and then sort the length

# If sorted by length and the alphabetically, the result would be a list
# that was sorted alphabetically with the strings of the same letters by increasing length
def main():
    words = fillList(filename="String.txt")
    sortAlphabetically(words)
    sortLength(words)
    print(words)

# The alternative method uses pythons build in sort function
# First it sorts the list alphabetically, and the by length


def alternativeMethod():
    secondWords = fillList(filename="String.txt")
    print(sorted(sorted(secondWords), key=len))


main()
# output: ['a', 'b', 'c', 'c', 'aa', 'aa', 'bb', 'cc', 'dd', 'bbbbbbb']

alternativeMethod()
# output: ['a', 'b', 'c', 'c', 'aa', 'aa', 'bb', 'cc', 'dd', 'bbbbbbb']
