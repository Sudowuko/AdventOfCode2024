"""
Update:
- Antinodes exists along any grid location along the line created by a pair of nodes (same distance from each other)
Algorithm Update:
- Add while loops:
    - one for adding antinodes along one direction until out of bounds
    - one for adding anunodes along other direction until out of bounds
- keep using set so that you keep antinode locations unique
Corner Case while coding:
- the nodes that create the antinode line are also antinodes
    - Make newLocs equal to the initial nodes first
"""

from collections import defaultdict

antinodes = set()
freqLocs = defaultdict(list)
inputMap = []
numLocs = 0

#Create inputmap
with open('8_input.txt', 'r') as file:
    for line in file:
        inputMap.append(list(line[:-1]))

numR = len(inputMap)
numC = len(inputMap[0])

#Populate frequency locations
for r in range(numR):
    for c in range(numC):
        if inputMap[r][c] != ".":
            freqLocs[inputMap[r][c]].append((r, c))

#Populate location set
for freq, locs in freqLocs.items():
    for first in range(len(locs)):
        for second in range(first + 1, len(locs)):
            rDisp = locs[second][0] - locs[first][0]
            cDisp = locs[second][1] - locs[first][1]

            

            newLoc1 = (locs[second][0], locs[second][1])
            newLoc2 = (locs[first][0], locs[first][1])

            while newLoc1[0] in range(numR) and newLoc1[1] in range(numC):
                antinodes.add(newLoc1)
                newLoc1 = (newLoc1[0] + rDisp, newLoc1[1] + cDisp)

            while newLoc2[0] in range(numR) and newLoc2[1] in range(numC):
                antinodes.add(newLoc2)
                newLoc2 = (newLoc2[0] - rDisp, newLoc2[1] - cDisp)

for antinode in antinodes:
    inputMap[antinode[0]][antinode[1]] = "#"

for line in inputMap:
    print("".join(line))

print(len(antinodes))