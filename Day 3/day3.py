#day 2
#read from text file
text_file = open("testdata.txt", "r")
lines = text_file.readlines() #global
#print(lines)


"""
#convert all to int and make new list
betterlines = []
for line in lines:
    newline = int(line)
    betterlines.append(newline)
"""
#print(betterlines)

def is_0or1_most(index):
    numones = 0
    numzeros = 0
    mostcommon = "error" #set to 0 or 1
    for line in lines:
        if line[index] == "1": #data file contains strings
            numones += 1
        elif line[index] == "0":
            numzeros += 1
    if numones == 0 and numzeros == 0: #in case it gets to /n at the end
        print("error no ones or zeros")
        return mostcommon
    #determine if more ones or zeros
    if numones > numzeros:
        mostcommon = "1"
    elif numones < numzeros:
        mostcommon = "0"
    else:
        #ones and zeros are equal
        mostcommon = "1"
        print("equal amounts of 1 and 0")
    return mostcommon


#determine oxygen generator rating
oxygen_generator_rating = "null"
remaininglines = [] #store the binary numbes not yet eliminated from list
print("remaininglines at beginning")
print(remaininglines)


#loop through lines once at index 0
digit = is_0or1_most(0)
print(digit)
for line in lines:
    if line[0] == digit:
        remaininglines.append(line)
print("remaininglines after first iteration")
print(remaininglines)


lines= [] #empty the list
#then loop through remaininglines
#skip index 0
#range(1, 5) will count 1234
for index in range(1, 5):#5 for test data, 12 for real data
    digit = is_0or1_most(index)
    print(digit)
    for line in remaininglines:
        if line[index] == digit:
            lines.append(line)
    print("remaininglines at index",index, remaininglines)
    print("lines at index",index, lines)
    if len(remaininglines) == 1: #if there is only 1 number left
        oxygen_generator_rating = remaininglines[0] #first and only values in list

print(remaininglines)
print("oxygen_generator_rating is", oxygen_generator_rating)
"""
for i in range(12): #5 for test data, 12 for real data
    print(i)

   
#convert to decimal
#note: bin() is used to go from binary to decimal
gamma_int = int(gamma, 2) # 2 us because we are staring in binary (base 2)
epsilon_int = int(epsilon, 2)

print("gamma as decimal", gamma_int)
print("epsilon as decimal", epsilon_int)

answer = gamma_int*epsilon_int

print("gamma*epsilon =",answer)
"""

input("press enter to exit")
