# Greg Ryterski
# 01/31/2022
# gjr7dz, 18186949

# This function is removing words that don't have the characters in the
# correct position in the list of 5-letter words.
def reduceWords(letter, words, pos):
    res = list(filter(lambda x: x[pos] == letter, words))
    return res

# This function is removing words that contain characters that are not
# in the word.
def checkChar(letter, words):
    res = list(filter(lambda x: letter not in x, words))
    return res

#Opens the file for the 5-letter Words and Used Words which is the
# previously used wordle words.
fileObj = open("5-LetterWords.txt", "r")
words = fileObj.read().splitlines()
fileObj.close()

fileObj2 = open("UsedWords.txt", "r")
usedWords = fileObj2.read().splitlines()
fileObj2.close()

# Removes any of the previously used words from all the other 5-letter
# words because it's unlikely that the word will appear again.
for x in words:
    for y in usedWords:
        if x == y:
            words.remove(x)
            
# Counts then prints how many words are still possible to guess
count = 0
for x in words:
    count+=1

print("There are:", count, "words\n")

print("\n")
k = 1
guessCount = 0
realWord = ["0","0","0","0","0"] # A list containing correct chracters if they're in the
                                 # correct position.

# Loops the program to run until the user gets the right word or runs through 5 guesses.
while True:
    i = 1
    while i == 1: # Error checks the input guess word provided by the user
        guessWord = input("Guess a word: ")
        guessWord = guessWord.lower()
        if(len(guessWord) == 5):
            if guessWord in words:
                print("The word is valid\n")
                i = 0
            else:
                print("The word is invalid\n")
                i = 1
        else:
            continue

    count = 0

    # Prompts the user to answer questions about the letters in the word they guessed
    firstPos = input("Is the letter {} in the word (y/n): ".format(guessWord[0]))
    if firstPos == "y":
        firstCPos = input("Is the letter {} in the correct position of the word (y/n): ".format(guessWord[0]))
        if firstCPos == "y":
            realWord[0] = guessWord[0]
            words = reduceWords(guessWord[0], words, 0)
    else:
        words = checkChar(guessWord[0], words)

    secondPos = input("Is the letter {} in the word (y/n): ".format(guessWord[1]))       
    if secondPos == "y":
        secondCPos = input("Is the letter {} in the correct position of the word (y/n): ".format(guessWord[1]))
        if secondCPos == "y":
            realWord[1] = guessWord[1]
            words = reduceWords(guessWord[1], words, 1)
    else: 
        words = checkChar(guessWord[1], words)

    thirdPos = input("Is the letter {} in the word (y/n): ".format(guessWord[2]))
    if thirdPos == "y":
        thirdCPos = input("Is the letter {} in the correct position of the word (y/n): ".format(guessWord[2]))
        if thirdCPos == "y":
            realWord[2] = guessWord[2]
            words = reduceWords(guessWord[2], words, 2)
    else: 
        words = checkChar(guessWord[2], words)

    fourthPos = input("Is the letter {} in the word (y/n): ".format(guessWord[3]))
    if fourthPos == "y":
        fourthCPos = input("Is the letter {} in the correct position of the word (y/n): ".format(guessWord[3]))
        if fourthCPos == "y":
            realWord[3] = guessWord[3]
            words = reduceWords(guessWord[3], words, 3)
    else: 
        words = checkChar(guessWord[3], words)

    fifthPos = input("Is the letter {} in the word (y/n): ".format(guessWord[4]))
    if fifthPos == "y":
        fifthCPos = input("Is the letter {} in the correct position of the word (y/n): ".format(guessWord[4]))
        if fifthCPos == "y":
            realWord[4] = guessWord[4]
            words = reduceWords(guessWord[4], words, 4)
    else: 
        words = checkChar(guessWord[4], words)

    # Asks if the word they were looking for is correct            
    actualWord = input("Is {} the 5-letter word you're looking for(y/n): ".format(guessWord))
    if(actualWord == "y"):
        print("\nCongrats!!!\n")
        break
    else:
        try:
            words.remove(guessWord) # Tries to remove the word if it isn't correct
        except:
            pass
    
    print("\n", realWord) # Prints the list containing characters that are correct

    guessCount += 1
    print("You've tried:", guessCount, "time(s)\n") # Lets the user know how many times they've guessed

    # Counts then prints how many words are still possible to guess
    for x in words:
        count+=1

    print("There are:", count, "words left\n")

    # Prints the possible words if there are less than 300 left
    if(count <= 300):
        for word in words:
            print(word)
