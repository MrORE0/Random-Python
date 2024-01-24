#Task 1-A
# fileOUT = open("debanks.txt", "r")
# lyrics = fileOUT.readline()
# line = 1
# while lyrics != "":
#     lyrics = lyrics.strip("\n")
#     print(line, lyrics)
#     lyrics = fileOUT.readline()
#     line += 1
# fileOUT.close()


# Task 1-B
# fileOUT = open("debanks.txt", "r")
# lyrics = fileOUT.read()
# line = 1
# lyrics = lyrics.split("\n")
# for lyric in lyrics:
#     print(line, lyric)
#     line += 1
# fileOUT.close()

# Task 1-C
# fileOUT = open("debanks.txt", "r")
# lyrics = fileOUT.readlines()
# line = 1
# for lyric in lyrics:
#     lyric = lyric.strip("\n")
#     print(line, lyric)
#     line += 1
# fileOUT.close()


# Task 1-D
fileOUT = open("debanks.txt", "r")
for line, lyric in enumerate(fileOUT,1) :
    lyric = lyric.strip("\n")
    print(line, lyric)
fileOUT.close()
