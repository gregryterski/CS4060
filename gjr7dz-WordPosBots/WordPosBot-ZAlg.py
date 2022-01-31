# Greg Ryterski
# 01/27/2022
# gjr7dz, 18186949

# KMP search for words in the U.S. Consitution that is case in-senseitive.
# Finds all occurences of the pattern typed in by the user. The wordst case
# complexity of this algorihtm is O(n).


def KMPAlgorithm(pattern, words):
    n = len(words) # length of the Consitution
    m = len(pattern) # length of the pattern

    lps = [0]*m # Makes an array of m size filled with 0s
                # lps stands for longest proper prefix (suffix)
    
    pIndex = 0 # Index of pattern
    wIndex = 0 # Index of words
    numOfFinds = 0 # Number of found patterns in the document
    
    while wIndex < n:
        # Increments at the beginning and almost each time
        if pattern[pIndex] == words[wIndex]:
            wIndex += 1
            pIndex += 1 #Increments the found word index

        # Checks to see if the pattern is found by checking if the index of the pattern is equal to
        # the size of the pattern
        if pIndex == m:
            print("Pattern is found at index: {}".format(str(wIndex-pIndex)))
            numOfFinds += 1
            pIndex = lps[pIndex-1]

        # Pattern not found so change either the index of the words or set the
        # index of the pattern to another value of the lps
        elif wIndex < n and pattern[pIndex] != words[wIndex]:
            if pIndex != 0:
                pIndex = lps[pIndex-1]
            else:
                wIndex += 1
    return numOfFinds # Returns the number of successful finds of the given pattern


# Creates a file object that reads in the Constitution and prompts the user
# to enter a pattern that they want to find in the Consitution. Both the
# Consitution and pattern are converted to lower case in order to find all
# occurences in the document regardless of casing. Also prints out the number
# of found occurences in the document.

fileObj = open("Constitution.txt", "r")
words = fileObj.read()
print("\nKMP Algorithm Search Algorithm for the Consitution\n")
pattern = input("Please enter the word pattern you want to search for: ")
print("")
#Making the words & pattern lower case so it should find all instances of the words
words = words.lower()
pattern = pattern.lower()
numOfFinds = 0
numOfFinds = KMPAlgorithm(pattern,words)
if numOfFinds > 0:
    print("\nThis pattern is found: {} time(s)".format(numOfFinds))
else:
    print("There were no occurences of the pattern: {}".format(pattern))
fileObj.close()

