#read from text file
text_file = open("day1data.txt", "r")
lines = text_file.readlines()


#convert all to int and make new list
betterlines = []
for line in lines:
    newline = int(line)
    betterlines.append(newline)

print(betterlines)


number1A = betterlines[0]
number2A = betterlines[1]
number3A = betterlines[2]

number1B = betterlines[3]
number2B = betterlines[4]
number3B = betterlines[5]
print("len")
print((len(betterlines)))

def averageof3(num1,num2,num3):
    total = num1+ num2 +num3
    average =total/3
    return average

def sumof3(num1,num2,num3):
    total = num1+ num2 +num3
    return total

print(str(averageof3(3,2,3)))

numincreases = 0
for i in range(0, len(betterlines)-2):
    number1B = betterlines[i]
    number2B = betterlines[i+1]
    number3B = betterlines[i+2]
    if sumof3(number1A,number2A,number3A) < sumof3(number1B,number2B,number3B):
        numincreases += 1
    number1A = number2A
    number2A = number3A
    number3A = number1B
           
print("numincreases is",numincreases)


#higher than 180
#lower than 1807
input("press enter to exit")
