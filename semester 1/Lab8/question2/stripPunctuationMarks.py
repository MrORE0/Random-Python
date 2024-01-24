puncMarks = [",", ".", "?", "-", "’", "!", ":", ";"]

def stripPunctuationMarks(text):
    words = text.split(' ')
    
    for _ in range(2):  # Check twice
        for i in range(len(words)):
            word = words[i]
            stripped_word = ''
            for char in word:
                if char in puncMarks:
                    stripped_word += char
            words[i] = word.strip(stripped_word)

    return words

print(stripPunctuationMarks('Contractions include: don’t, isn’t, and wouldn’t!'))
