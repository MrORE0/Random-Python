#Input
#ask the employee for how many hours are they working in a week

#Function
#get their working hours and for every hour he earns multiply that by 12 euro
#but for every hour that is above the standard (40) multiply by 20
#then add the up to see the total

#Output
#display the paycheck for the standard working hours and then for the overtime,then display the combined value of the two paycheck
working_hours = int(input("How many hours are you working per week? "))
if working_hours <=40:
    standard_pay = working_hours * 12
else:
    overtime_hours = working_hours - 40 #here we get the overtime by seeing what is left after the standard 40 hours
    working_hours -= overtime_hours #here we get what is left of the working hours if it was not fixed on 40
    standard_pay = working_hours * 12 # or you just write 40 * 12 because that should be the leftover
    overtime_pay = overtime_hours * 20
print("Basic pay: %i" % (standard_pay))
print("Overtime pay: %i" % (overtime_pay))
print("Total pay: ", standard_pay + overtime_pay)
