def readDraw(lotteryNums):
    outFile = open(lotteryNums, 'r')
    lines = outFile.readlines()
    lotteryDraws = []
    for line in lines:
        line = line.strip('\n')
        line = line.split(' ')
        int_list = []
        for item in line:
            int_list.append (int(item))
        lotteryDraws.append(int_list)
    return lotteryDraws

def checkWinners (lotteryDraws):
    lotteryDraws.sort()
    userInput = input('Enter your lucky numbers(with space between each number): ')
    userInput = userInput.strip('\n')
    userInput = userInput.split(' ')
    userList = []
    for number in userInput:
            userList.append (int(number))
    userList.sort()
    if userList in lotteryDraws:
         print('Congratulations, you just won a bunch of money!')
    else:
         print('Sorry, better luck next time.')
    return

lotteryDraws = readDraw('lotteryNumbers.txt')
checkWinners(lotteryDraws)
#for testing you can use the simple 1-6 for a success
