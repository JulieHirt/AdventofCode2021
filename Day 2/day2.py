#day 2
#read from text file
text_file = open("day2data.txt", "r")
lines = text_file.readlines()


print(lines)


#takes a line as input such as "forward 7" or "up 8"
#returns the movement command (up down forward) and the number of spaces
def getcommand(inputline):
    """returns the direction and number of spaces"""
    index = 0
    for i in inputline:
        if i == " ":
            break #stop when it gets to a space
        index += 1
    print("the space is at index", index)
    movementcommand = inputline[:index]
    numspaces = inputline[index+1:index+2]
    print("the letters before the space are", inputline[:index])
    print("the number right after the space is", inputline[index+1:index+2])
    return movementcommand,numspaces    

getcommand("down 4\n")

"""
#convert all to int and make new list
betterlines = []
for line in lines:
    newline = int(line)
    betterlines.append(newline)

#print(betterlines)
"""

input("press enter to exit")
