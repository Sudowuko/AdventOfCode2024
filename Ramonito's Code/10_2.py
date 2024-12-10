"""
Update:
- instead of calculating score, we want to calculate rating
    - rating is the number of unique hiking trails that lead to a 9
Change:
- Could instead look for 0s from the 9s
- but could also just add to the trailhead score if a 9 is included in the set
    - this wont work, because 9 will be in the visited so it wont be traversed again
    - change it so that when you encounter a 9 just increase rating and dont add
    it to visited
    - this way other paths that get to that 9 will also increase rating
Things I realized while coding:
- visited nodes from one path may be used in another path
    - since we keep them in visited, other paths may not be traversed
    - what if we remove the visited set?
        - you can never run into a cycle because you are going in ascending
        order of altitude, so it is impossible to create a cycle from that
        - oh wow this worked LOL
        - I guess you have to assume the graph created when following the 
        ascending rule is acyclic, because there cannot be unique paths once
        a cycle is present. And if it is acyclic, then each node that can
        reach a 9, will reach a 9, even if it passes over other nodes that have
        been traversed already
"""

from collections import deque

trailMap = []
result = 0
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

with open('10_input.txt', 'r') as file:
    for line in file:
        trailMap.append(list(line[:-1]))

numR = len(trailMap)
numC = len(trailMap[0])

def getTrailHeadScore(initR, initC):
    queue = deque()
    queue.append((initR, initC))
    rating = 0

    while queue:
        node = queue.pop()
        r, c = node
        alt = ord(trailMap[r][c])

        if alt == 57:
            rating += 1
        else:
            for dR, dC in directions:
                newR = r + dR
                newC = c + dC

                if newR in range(numR) and newC in range(numC):
                    newAlt = ord(trailMap[newR][newC])
                    if newAlt > 46 and newAlt == alt + 1:
                        queue.append((newR, newC))

    return rating

for r in range(numR):
    for c in range(numC):
        if trailMap[r][c] == "0":
            result += getTrailHeadScore(r, c)

print(result)