def BinarySearch(numberToFind, L):

    # high and low are essentially the limits within we search
    low = 0
    high = len(L)-1
    mid = (low+high)//2

    while low<=high: #because we want to end when they pass each other indicating that the number was not found
        if L[mid] == numberToFind:
            return mid
        elif L[mid] <= numberToFind:
            low = mid + 1 #moving the low so we search only the right side of the list
        else:
            high = mid -1   #moving the high so we search only the left side of the list
        mid = (low+high)//2 #calculating the new midpoint
    return None #if nothing was find then there is no such number inside the list

numberToFind = int(input("Enter a number to be found: "))
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Your number was found at position:", BinarySearch(numberToFind, L))
