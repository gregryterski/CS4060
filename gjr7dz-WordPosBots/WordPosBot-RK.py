# Greg Ryterski
# 01/30/2022
# gjr7dz, 18186949

NO_OF_CHAR = 256 # Number of characters in the alphabet

# Searches for the given pattern by the user in the Consitution. The best-case
# running time of this algorithm is O(n+m) and worst-case is O(nm).

# The q stands for a prime number and the other parameters are explanatory.
def search(words, pattern, q):
    n = len(words) # length of the Constitution
    m = len(pattern) # length of the pattern
    i = 0
    j = 0
    k = 0 # hash value of the pattern
    l = 0 # hash value of the words
    h = 1
    
    for i in range(m-1):
        h = (h*NO_OF_CHAR)%q

    for i in range(m): # Gets the hash values for the pattern and words
        k = (NO_OF_CHAR*k + ord(pattern[i]))%q
        l = (NO_OF_CHAR*l + ord(words[i]))%q

    # Linear slide of the pattern over the words
    for i in range(n-m+1):
        if k == l: # Checks if the hash values of the words and pattern are the same
            for j in range(m):
                if words[i+j] != pattern[j]:
                    break
                else:
                    j += 1

            if j == m: # Pattern is found
                print("Pattern is found at the index: {}".format(i))

        if i < n-m: # Gets the next hash value for words by remvoing leading digit
                    # and adds trailing digit
            l = (NO_OF_CHAR*(l-ord(words[i])*h) + ord(words[i+m]))%q

            if l < 0:
                l = l+q

# Creates a file object that reads in the Constitution and prompts the user
# to enter a pattern that they want to find in the Consitution. Both the
# Consitution and pattern are converted to lower case in order to find all
# occurences in the document regardless of casing. Also prints out the number
# of found occurences in the document.

fileObj = open("Constitution.txt", "r")
words = fileObj.read()
print("\nRabin-Karp Search Algorithm for the Consitution\n")
pattern = input("Please enter the word pattern you want to search for: ")
print("")
#Making the words & pattern lower case so it should find all instances of the words
words = words.lower()
pattern = pattern.lower()
q = 101
search(words, pattern, q)

