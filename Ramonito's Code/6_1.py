"""
Input:
- ^ or > or v or < -> the gaurd
- . -> open space
- # -> obstacle
Output:
- Given the gaurds initial starting position
    - Move the gaurd in its current direction until it hits an obstacle
    - On every obstacle, gaurd will turn 90 degrees and continue
    - Keep doing this until gaurd leaves map
- Find the number of points within the open space that the gaurd 
traversed. 
    - return the number of points
    - assumed gaurd can overlap themself, but still counts as one point
Approach + Algorithm:
- Create a list of directions
- Create a set of points that the gaurd has traversed
- Convert the input into a 2D matrix
    - can use same characters in input
    - keep note of where gaurd is once found
- while the gaurd is within the bounds of the input
    - save current coordinate in set of points
    - if next point along given direction is # switch direction
        - move to next direction in directions list
            - when reach end of list, go back to start
    - else move along current direction
- return length of set of coordinates
    - using a set so that duplicates wont be counted
- Time: O(n) going to traverse each node a finite amount of times
- Space: O(n) storing points traversed
Checks I did while coding:
- Checked if first positiong of gaurd is facing upwards (dont need to 
handle those edge cases)
- Added one more line before input to handle last line edge case
"""

#Define variables
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
currDir = 0
traversed = set()
inputMap = []
currR = None
currC = None

with open('6_input.txt', 'r') as file:
    for line in file:
        inputMap.append(list(line[:-1]))

numRows = len(inputMap)
numCols = len(inputMap[0])

for r in range(numRows):
    for c in range(numCols):
        if inputMap[r][c] == "^":
            currR = r
            currC = c

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

print(len(traversed))
        