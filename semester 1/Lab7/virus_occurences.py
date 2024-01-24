# The function should return a dictionary in which the keys are the names of locations in 
# the data file, and the value associated with each key is a list of the (integer) values 
# presenting the cumulative number of infections at that location. 

# Part A
def load_data(filename):
    outFile = open(filename, 'r')
    file = outFile.readlines()
    dictionary = {}
    for line in file:
        line = line.strip('\n')
        line = line.replace(' ', '') #so it can remove any arbitrary number of whitespace
        line = line.split(',')
        for i in range(1,len(line)):
            line[i] = int(line[i])
        dictionary[line[0]] = line[1:len(line)]
    return dictionary


occur = load_data('occurences.txt')
print(occur)

# Part B
def daily_cases(cumulative):
    new_dict = {}
    
    for location, cumulative_values in cumulative.items():
        # using the first value of every dict to start a list with the new values
        new_cases = [cumulative_values[0]] # Initialize with the first day's cumulative value
        for i in range(1, len(cumulative_values)):
            # Calculate the new cases for each day by subtracting the cumulative value of the previous day
            new_cases.append(cumulative_values[i] - cumulative_values[i - 1])#second minus first and third minus second
        new_dict[location] = new_cases

    return new_dict

occur2 = daily_cases(occur)
print(occur2)
