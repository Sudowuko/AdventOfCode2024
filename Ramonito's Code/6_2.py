"""
Update:
- New goal is to put the gaurd in a walking loop
- To achieve this you are able to place one obstacle 
(another # essentially) along its path
Output:
- Output the number places you can put this obstacle so that
the gaurd is put in a loop
Notes:
- The only relevant places you can put an obstacle is along
the already given path of the gaurd
    - Putting an obstacle on a point that the gaurd never traverses
    is useless
- Cannot put obstacle on starting position
Approach:
- Very Naive Approach but prob okay
    - Test placing the obstacle on every single possible coordinate
        - Keep track of two deque's (size 4)
        - every time you hit an obstacle, store its coordinate in the 
        first deque
        - once the first deque is filled, on every enqueue, deque the
        first one and enqueue into the second
        - once you both deques are full, do the same thing, 
        but dequeue from from second dequeue on every enqueue
            - also check if two deques are ever the same, 
            if they are, this means the cycle has been traversed twice,
            meaning that the gaurd is in a loop
        - if the gaurd leaves the map, this did not work
Corner Cases While coding:
- the last cycle can be created with more than 4 nodes in the cycle
Improvemebt:
- maybe just check if you have hit same objext from same direction twice
    - if this has happened, this means that upon hitting this object
    from a given direction, you will hit again from the same direction
    - which creates a never ending loop -> indicating a cycle
"""

from collections import deque

#Define variables
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
currDir = 0
traversed = set()
inputMap = []
currR = None
currC = None
initialR = None
initialC = None
result = 0

with open('6_input.txt', 'r') as file:
    for line in file:
        inputMap.append(list(line[:-1]))

numRows = len(inputMap)
numCols = len(inputMap[0])

for r in range(numRows):
    for c in range(numCols):
        if inputMap[r][c] == "^":
            initialR = currR = r
            initialC = currC = c

#Create traversed list
while currR in range(numRows) and currC in range(numCols):
    traversed.add((currR, currC))
    newR = currR + directions[currDir][0]
    newC = currC + directions[currDir][1]

    if newR in range(numRows) and newC in range(numCols) and inputMap[newR][newC] == "#":
        if currDir == 3:
            currDir = 0
        else:
            currDir += 1
    else:
        currR = newR
        currC = newC

#Traverse while iterating through every possible obstacle
for obsR, obsC in traversed:
    if obsR == initialR and obsC == initialC:
        continue

    inputMap[obsR][obsC] = "#"
    obsHit = set()
    currR = initialR
    currC = initialC
    currDir = 0

    while currR in range(numRows) and currC in range(numCols):
        newR = currR + directions[currDir][0]
        newC = currC + directions[currDir][1]

        if newR in range(numRows) and newC in range(numCols) and inputMap[newR][newC] == "#":
            if currDir == 3:
                currDir = 0
            else:
                currDir += 1
            
            if ((newR, newC), currDir) in obsHit:
                result += 1
                break
            else:
                obsHit.add(((newR, newC), currDir))
        else:
            currR = newR
            currC = newC
    
    inputMap[obsR][obsC] = "."


print(result)
        