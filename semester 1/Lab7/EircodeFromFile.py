OutFile = open('EirCodes.txt', 'r')
routingKeys = OutFile.readlines()
dictionary = {}
for line in routingKeys:
    line = line.strip('\n')
    items = line.split(' ')
    dictionary[items[0]] = items[1]

def validator(code):
    code = code.upper()
    codeList = list(code)
    codeList[0] = codeList[0]
    codeList[1] = codeList[1]
    codeList[2] = codeList[2]
    if (codeList[0].isalpha() == True) and (codeList[1].isnumeric() == True) and codeList[2].isnumeric() == True:
        if code in dictionary:
            print(dictionary[code])
        else:
            print('Your code was not found.')
    elif (codeList[0] == 'D') and (codeList[1] == '6') and codeList[2] == 'W':
        if code in routingKeys:
            print(routingKeys[code])
        else:
            print('Your code was not found.')
    else:
        print('Please make sure your code is right and follows it this pattern (A23), with exception for the code(D6W)')

code = input("Enter your Eircode: ")
validator(code)
OutFile.close()