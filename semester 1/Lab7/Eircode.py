#7 character unique code (3 char routing key, 4 char unique identifier for your home address)
# The routing key is the first 3 characters of an Eircode and identifies an area/townland. 
# The first character is always a letter, followed by 2 numbers (except for D6W). 
# The unique identifier is a group of 4-characters and is unique to your home or premises.

# Create a program that reads in a postal code from the user and display the townland associated with it
# e.g. if the user enters W23, the program will return Cellbridge. Assume you have a hard coded 
# dictionary to represent the routing keys as displayed in the above table. Display a meaningful error 
# if this is not a legitimate eircode.

routingKeys = {'A63': 'Greystones', 'A98':'Bray', 'P17':'Kinsale', 'A86':'Dunboyne', 'W23':'Cellbridge', 'F45':'Castlerea', 'F35':'Ballyhaunis', 'H14':'Belturbet', 'N39':'Longford', 'F56':'Ballymote'}

def validator(code):
    code = code.upper()
    codeList = list(code)
    codeList[0] = codeList[0]
    codeList[1] = codeList[1]
    codeList[2] = codeList[2]
    if (codeList[0].isalpha() == True) and (codeList[1].isnumeric() == True) and codeList[2].isnumeric() == True:
        if code in routingKeys:
            print(routingKeys[code])
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