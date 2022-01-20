#day 2
#read from text file
text_file = open("testdata.txt", "r")
lines = text_file.readlines()
#print(lines)

"""
#convert all to int and make new list
betterlines = []
for line in lines:
    newline = int(line)
    betterlines.append(newline)
"""
#print(betterlines)

#just doing the first digit in each line
for line in lines:
    print(line[0]) #print the first digit in the line


input("press enter to exit")
