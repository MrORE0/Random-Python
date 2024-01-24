fileOUT = open("dna.txt", "r")
text = fileOUT.read()

dna = text.split("\n\n")
id = 0
for person in dna:
    id +=1
    print(id, person)

fileOUT.close()