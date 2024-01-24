counter = int(input('Choose a number: '))
def  blastoffFor(counter):
    for nums in range (counter):
        if counter != 0:
            print(counter)
            counter -=1
    print('Blast Off')
def  blastoffWhile(counter):
    while counter>0:
        print(counter)
        counter-=1
    print('Blast Off')
blastoffWhile(counter)
