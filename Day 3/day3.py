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
numones = 0
numzeros = 0
gamma = ""
for line in lines:
    if line[0] == "1": #data file contains strings
        numones += 1
    elif line[0] == "0":
        numzeros += 1
#determine if more ones or zeros and add correponding number to answer
#this is to calculate gamma rate
if numones > numzeros:
    gamma = gamma + "1"
elif numones < numzeros:
    gamma = gamma + "0"
else:
    #ones and zeros are equal
    print("error, equal amounts of 1 and 0")
    
print("numones is", numones)
print("numzeros is", numzeros)
print("gamma is", gamma)
        
        


input("press enter to exit")
