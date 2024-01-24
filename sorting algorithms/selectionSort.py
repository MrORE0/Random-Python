l = [2, 4, 5, 6, 3, 1, 9, 8, 11, 88, 99, 78, 61, 23, 63]

def selectionSort(List):
    counter = 0

    while counter < len(List):
        temp = max(List[:len(List) - counter]) #gets the maximum value thats inside the list
        tempIndex = List.index(temp) #gets the index of the maximum value so we can use it to swap the numbers
        #gets the last value of the list and gets one less every time because the next is going to be smaller
        #than the previous
        last = List[-(counter + 1)] 
        List[-(counter + 1)] = temp #puts the biggest value at the end
        List[tempIndex] = last #puts the last value at the place of the max(swapping their places)
        counter += 1 #updates the counter so the loop can end eventually
    return List #returns the sorted list

print(selectionSort(l))


