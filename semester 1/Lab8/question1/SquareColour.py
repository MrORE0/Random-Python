def getSquareColor (row, col):
    if 0<=row<=7 and 0<=col<=7:
        if row % 2 == 0 and col % 2 == 0:
            print("white")
        elif row % 2 != 0 and col % 2 != 0:
            print("white")
        else:
            print("black")
    else:
        print("The numbers should be in the range 0-7")

getSquareColor(0, 1)