# def romanNumeralMatch(num):
#     match num:
#         case 1:
#             print('I')
#         case 2:
#             print('II')
#         case 3:
#             print('III')
#         case 4:
#             print('IV')
#         case 5:
#             print('V')
#         case 6:
#             print('VI')
#         case 7:
#             print('VII')
#         case 8:
#             print('VIII')
#         case 9:
#             print('IX')
#         case 10:
#             print('X')
#         case _:
#             print('Error, the number is out ot range 1-10')


# def romanNumeral(num):
#     if num == 1:
#         print('I')
#     elif num == 2:
#         print('II')
#     elif num == 3:
#         print('III')
#     elif num == 4:
#         print('IV')
#     elif num == 5:
#         print('V')
#     elif num == 6:
#         print('VI')
#     elif num == 7:
#         print('VII')
#     elif num == 8:
#         print('VIII')
#     elif num == 9:
#         print('IX')
#     elif num == 10:
#         print('X')
#     else:
#         print('Error, the number is out ot range 1-10')

def romanNumerallist(num):
        if num in numbers:
            index = numbers.index(num)
            print(r_numerals[index])

        else:
            print('Error, the number is out ot range 1-10')


numbers = [1,2,3,4,5,6,7,8,9,10]
r_numerals = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
num = int(input('Enter a number 1-10: '))
romanNumerallist(num)
