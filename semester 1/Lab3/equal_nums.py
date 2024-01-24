import math

def equal_numbers(num1, num2):
    if num1 == num2:
        print(float(math.sqrt(num1)))
    else:
         print(num1**2)

equal_numbers(int(input("First number: ")), int(input("Second number: ")))
