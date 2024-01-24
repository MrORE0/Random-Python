def bubbleSort(list):
    temp = 0
    counter = 0
    if list == []:
        return list
    else:
        for item in range(len(list)-1):
            if list[item] > list[item+1]:
                temp = list[item+1]
                list[item+1] = list[item]
                list[item] = temp
            else:
                counter += 1
        if counter != len(list)-1:
            return bubbleSort(list) # idk why but to recurse you need to type return before that
        else:
            return list
   #you can make it break when it counter is in one less the the length of the list
random_list = [5, 2, 9, 1, 5, 6, 3, 8, 7, 4]

print(bubbleSort(random_list))