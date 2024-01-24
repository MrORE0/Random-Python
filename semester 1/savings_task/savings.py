# Write a program called savings.py to see how many years it will take a bank account to grow 
# to a specified value, assuming a fixed annual interest. Prompt the user for three numbers:
#  an initial balance, the annual percentage for interest as a decimal e.g. .04 for 4%, 
# and the final balance desired. Print the initial balance, and the balance each year 
# until the desired amount is reached. Round displayed amounts to two decimal places.

# (Note: The amount for next year is determined as the current balance times (1 + interest fraction). 
# So if the balance is €500 now and the interest rate is .04, there is €500*(1.04) = €520 after one year 
# and after two years €520*(1.04) = €540.80. 



initialBalance = float(input("Please enter your initial balance: "))
annualInterest = float(input("Please enter the annual interest %: "))
balanceWanted = float(input("Please enter your desired balance: "))

def calculations(initialBalance, annualInterest, balanceWanted):
    while initialBalance <= balanceWanted:
        print("%.2f" % initialBalance)
        initialBalance *= 1 + annualInterest
    print("%.2f" % initialBalance)

calculations(initialBalance, annualInterest, balanceWanted)