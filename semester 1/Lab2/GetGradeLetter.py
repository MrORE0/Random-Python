gradePercentage = int(input("Please enter your numerical grade: "))
if gradePercentage >=0 and gradePercentage <= 24:
    print("F")
elif gradePercentage >=25 and gradePercentage <= 39:
    print("E")
elif gradePercentage >=40 and gradePercentage <= 54:
    print("D")
elif gradePercentage >=55 and gradePercentage <= 69:
    print("C")
elif gradePercentage >=70 and gradePercentage <= 84:
    print("B")
elif gradePercentage >=85 and gradePercentage <= 100:
    print("A")
else:
    print("X")
