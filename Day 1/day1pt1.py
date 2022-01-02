#read from text file
text_file = open("day1data.txt", "r")
lines = text_file.readlines()


#convert all to int and make new list
betterlines = []
for line in lines:
    newline = int(line)
    betterlines.append(newline)

print(betterlines)


number1 = betterlines[0]
print("len")
print((len(betterlines)))

numincreases = 0
for i in range(1, len(betterlines)):
    number2 = betterlines[i]
    if number2 > number1:
        numincreases += 1
    number1 = number2
           
print("numincreases is",numincreases)
    
input("press enter to exit")
