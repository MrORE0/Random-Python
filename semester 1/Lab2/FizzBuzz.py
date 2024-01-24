number = int(input("Choose a number: "))
#remember there is a structure in conditions and thats is why we put this condition first, because we need to check for it
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 ==0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
