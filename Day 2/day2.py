#day 2
#read from text file
text_file = open("day2data.txt", "r")
lines = text_file.readlines()
#print(lines)

#takes a line as input such as "forward 7" or "up 8"
#returns the direction (up down forward) and the number of spaces
def getcommand(inputline):
    """returns the direction and number of spaces"""
    index = 0
    for i in inputline:
        if i == " ":
            break #stop when it gets to a space
        index += 1
    direction = inputline[:index]
    numspaces = inputline[index+1:index+2]
    #print("the letters before the space are", inputline[:index])
    #print("the number right after the space is", inputline[index+1:index+2])
    return direction, numspaces    



def move(aim, direction, numspaces, horizontalposition, depth):
    """calculates new position based on movement command"""
    numspaces = int(numspaces)
    if direction == "down":
        aim += numspaces
    elif direction == "forward":
        horizontalposition += numspaces
        depthincreaseamt = aim*numspaces
        depth += depthincreaseamt
    elif direction == "up":
        aim -= numspaces
    else:
        print("warning! invalid direction given! No movement.")
    return horizontalposition, depth, aim

#horizontalposition and depth are calculated based on the movements
#ie "forward 5" adds 5 to horizontalposition
horizontalposition = 0
depth = 0
aim = 0
#loop through each command and move the ship
for line in lines:
    #print(line)
    direction, numspaces = getcommand(line)
    horizontalposition, depth, aim = move(aim, direction, numspaces, horizontalposition, depth)


print("horizontalposition: ", horizontalposition, "depth: ", depth)

print("horizontalposition*depth =", horizontalposition*depth)

"""
#convert all to int and make new list
betterlines = []
for line in lines:
    newline = int(line)
    betterlines.append(newline)

#print(betterlines)
"""

input("press enter to exit")
