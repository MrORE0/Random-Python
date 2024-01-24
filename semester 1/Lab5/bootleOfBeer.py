# def bottlesOfBeer(numberOfBottles):
#     if numberOfBottles !=0:
#         print(f'{numberOfBottles} bottles of beer on the wall, {numberOfBottles} bottles of beer. Take one down and pass it around, {numberOfBottles-1} of beer on the wall')
#         numberOfBottles-=1
#         bottlesOfBeer(numberOfBottles)
# here you are missing to change bottles to bottle when it comes to the last two lines

# try to use only while and not if

def bottlesOfBeer(numberOfBottles):
    while numberOfBottles != 0:
        if numberOfBottles == 2:
            print(f'{numberOfBottles} bottles of beer on the wall,{numberOfBottles} bottles of beer. Take one down and pass it around,{numberOfBottles-1} bottle of beer on the wall')
            numberOfBottles-=1
        elif numberOfBottles == 1:
            print(f'{numberOfBottles} bottle of beer on the wall, {numberOfBottles} bottle of beer. Take one down and pass it around, {numberOfBottles-1} bottle of beer on the wall')
            numberOfBottles-=1
        else:
            print(f'{numberOfBottles} bottles of beer on the wall, {numberOfBottles} bottles of beer. Take one down and pass it around, {numberOfBottles-1} bottles of beer on the wall')
            numberOfBottles-=1
bottles = int(input('Enter number of bottles: '))
bottlesOfBeer(bottles)
