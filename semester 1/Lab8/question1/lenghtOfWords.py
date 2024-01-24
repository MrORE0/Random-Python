# We want a function called getWordLengths() that accepts a piece of text (string) as input and 
# returns a list of integers i.e. the lengths of each word in the piece of text.

# getWordLengths (‘This is the CS1117 exam’) => [4,2,3,6,4]
def getWordLengths(text):
    wordLength = []
    words = text.split(" ")
    for word in words:
        chars = 0
        for char in word:
            chars += 1
        wordLength.append(chars)
    print(wordLength)

getWordLengths("This is the CS1117 exam")

