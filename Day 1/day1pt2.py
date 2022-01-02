#day 1 part 2

import math 
#read from text file
text_file = open("day1data.txt", "r")
lines = text_file.readlines()


#convert all to int and make new list
betterlines = []
for line in lines:
    newline = int(line)
    betterlines.append(newline)

#print(betterlines)

def sumof3(num1,num2,num3):
    total = num1+ num2 +num3
    return total

prevsum = math.inf #set first sum to infinity so it will not measure an increase
nextsum = 0
numincreases =0 #use to count the number of times the sliding sum increased

#divide into sliding sets of 3 and print all sets
#for i in range(len(betterlines)):
for i in range(len(betterlines)-2):
    index1 = i
    index2 = i+1
    index3 = i+2
    nextsum = sumof3(betterlines[index1], betterlines[index2], betterlines[index3])
    if nextsum > prevsum:
        numincreases += 1
    prevsum= nextsum #set up for next time in loop
    
    #print("indexes", index1," ",index2, " ", index3)
    #print("set of 3 numbers",betterlines[index1]," ", betterlines[index2]," ", betterlines[index3])
    
    


print("numincreases is", numincreases)


input("press enter to exit")
