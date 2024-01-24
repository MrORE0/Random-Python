num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))

def sameOrDifferent(num1, num2, num3):
    if  num1 == num2 == num3:
        print('They are the same.')
    else:
        print('They are not the same.')

sameOrDifferent(num1, num2, num3)

# sameOrDifferent(num1 = int(input('Enter the first number: ')),
# num2 = int(input('Enter the second number: ')),
# num3 = int(input('Enter the third number: ')))