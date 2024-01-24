
def calculateBill(minutes, messages):
    base = 15.00

    if minutes <= 50 and messages <=50:
        tax = base * 0.05
        total = base + tax
        print('The total bill is %.2f' % total)

    else:
        print('The basic bill is %.2f' % base)

        if  minutes > 50:
            minutes -= 50
            minutes *= 0.25
            print('Additional minutes: %.2f' % minutes)
            base += minutes

        if messages > 50:
            messages -=50
            messages *= 0.15
            print('Additional messages: %.2f' % messages)
            base += messages
         
        tax = base * 0.05 
        total = base + tax

        print('Total bill is: %.2f' % total)
        


used_minutes = int(input('How many minutes have you used this mont: '))
used_messages = int(input('How many text messages have you used this month: '))
calculateBill(used_minutes, used_messages)