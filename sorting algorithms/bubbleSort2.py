# this version just doesn't use the len() function from python
def bubbleSort(List):
    temp = 0
    nums = 0
    l = []
    counter = 0
    while l != List:
        l.append(List[nums])
        nums += 1

    for item in range(nums - 1):  
        if List[item] > List[item+1]:
            temp = List[item+1]
            List[item+1] = List[item]
            List[item] = temp
        else:
            counter += 1

    if counter != nums - 1:  
        return bubbleSort(List)
    else:
        return List

random_list = [5, 2, 9, 1, 5, 6, 3, 8, 7, 4]
print(bubbleSort(random_list))
