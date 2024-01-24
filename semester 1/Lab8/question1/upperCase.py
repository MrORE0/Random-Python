LOWER_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l':'L', 'm': 'M', 'n':'N', 'o':'O', 'p':'P', 'q':'Q', 'r':'R', 's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W', 'x':'X', 'y':'Y', 'z': 'Z'}

def toUpper (text):
    converted = ""
    for char in text:
        if char in LOWER_TO_UPPER:
            converted += LOWER_TO_UPPER[char]
        else:
            converted += char
    return converted

print(toUpper('hello'))
