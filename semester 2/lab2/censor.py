MASK = "*"

def generate_banned_words():
    #read banned words in from file bannedWords and return a list
    #of banned words
    
    #THIS IS WHERE YOU START (STEP 1)
    OutFile = open('bannedWords.txt', 'r')
    bannedWords = OutFile.readlines()
    bannedWords = list(map(lambda word:word.strip('\n'), bannedWords)) #removes the \n from the words
    OutFile.close()
    return bannedWords

def bleeped(word):
    # Return a cleaned version of parameter 'word' with
    # any black-listed word replaced by asterisks. Ignore any
    # non-letters at the beginning or end of 'word'.
    
    for badword in BANNED_WORDS:
        w = word.lower() #using another variable so we don't change the words which have capital letters
        if badword in w:
            word = w.replace(badword, MASK * len(badword))
    return word

def censor_line(line):
    # Return censored version of the text in string parameter
    # 'line' while preserving word breaks and punctuation. 
    
    #split the lines into words and return a clean version of the word by invoking the bleeped function
    words = line.split(' ')
    for i, word in enumerate(words):
        words[i] = bleeped(word)

    #if I didn't have the join thing below I would use that
    # for word in range(words)-1: #minus one we the last element, gets \n instead of space
    #     line += word + ' '
    # line += '\n'
    # return line
    return " ".join(words)

#because we made every word in lower case we need now to capitalize some of them

def censor_file(filename):
    # Generate a transformed version of the named text file containing
    # a censored version of the text.
    
    #THIS IS WHERE YOU COMPLETE STEP 2
    #This will invoke the function censor_line
    OutFile = open(filename, 'r')
    InFile = open('cleanText.txt', 'w')
    line = OutFile.readline()
    while line != '':
        line = censor_line(line)
        InFile.write(line)
        line = OutFile.readline()

    InFile.close()
    OutFile.close()
     

BANNED_WORDS = generate_banned_words()   
censor_file("someText.txt")

    