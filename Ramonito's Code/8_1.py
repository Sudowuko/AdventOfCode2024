"""
Input:
- grid of nodes
    - values: lower case letter, uppercase letter, digit, or "."
Output:
- want to find number of unique locations of antinodes
    - two antinodes are created for every pair of similar nodes
    - antinodes are placed perfeclty aligned with node pairs and must be twice as far away from one of the node pairs
    - both antinodes or places on either side of one of the nodes
Notes:
- once you get the row, column displacement between one pair of nodes:
    - one antinode is located at the same displacement starting from the second node
    - one antinode is located at the negative displacement at the current node
Algorithm:
- create set of existing antinode locations -> using set because want locations to be unique
- Use hashmap:
    - key: character
    - value: location of character (x, y)
    - can't have duplicate locations
- For every unique pair of locations for a character: loop throgh each loc, inner loop through each loc that comes after
    - calculate displacement
    - store both antinode locations in set using algorithm in Notes
        - if location is already in set, set will not update
        - if out of bounds, do not store
- Time: finite amount of characters, O(n^2) assuming that all characters are the same
- Space: O(n) -> hashmap and set
Corner Cases:
- if there is only one occurence of character, you have no antinodes
- as soon as there are more than one, you will have antinodes
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

            newLoc1 = (locs[second][0] + rDisp, locs[second][1] + cDisp)
            newLoc2 = (locs[first][0] - rDisp, locs[first][1] - cDisp)

            if newLoc1[0] in range(numR) and newLoc1[1] in range(numC):
                antinodes.add(newLoc1)
            if newLoc2[0] in range(numR) and newLoc2[1] in range(numC):
                antinodes.add(newLoc2)

for antinode in antinodes:
    inputMap[antinode[0]][antinode[1]] = "#"

for line in inputMap:
    print(line)

print(len(antinodes))