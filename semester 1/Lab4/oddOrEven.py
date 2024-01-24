
def oddOrEven(number):
    if  number % 2 == 0:
        return True
    else:
        return False
    

if oddOrEven(number = int(input('Choose a number: '))) == True:
    print('The number is even')
else:
    print('The number is odd')
