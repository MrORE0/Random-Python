retailChains = {'Aldi':['Cork', 'Kerry', 'Dublin', 'Waterford', 'Tralee'],
                'Tesco':['Cork', 'Limerick', 'Dublin', 'Dundalk', 'Tralee', 'Carlow', 'Waterford'],
                'Centra':['Cork', 'Dublin', 'Tullamore', 'Tralee']}

# def BiggestRetailChain(d):
#     greatestList = []
#     numberOfCities = 0
#     if len(d) > 0: #checking if its empty
#         max = 0 # variables to keep track of the max retailer
#         maxRet = ''
#         for retailer, cities in d.items(): #retailer here is the key and cities is the list corresponding
#             curLength = len(cities) # current length of our list
#             if curLength > max:
#                 max = curLength
#                 maxRet = retailer
#                 greatestList = retailChains[maxRet]

#     return greatestList
# list = BiggestRetailChain(retailChains)
# print(list)

def CommonTowns (d, rc1, rc2):
    towns = []
    for town2 in d[rc1]:
        if town2 in d[rc2]:
            towns.append(town2)
    return towns

list2 = CommonTowns(retailChains, 'Aldi', 'Tesco')
print(list2)