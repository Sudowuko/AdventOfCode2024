"""
Input:
- map of numbers and "."
    - 0 to 9
    - indicating altitude of ground at that location
    - "." indicates a non-passable ground
Output:
- Sum of trailhead scores
    - a trailhead starts at a 0
        - the score of a trailhead is how many unique 9s it can reach following a trail
        - a hiking trail is made from starting at a trail head and moving in the up, down,
        left, right directions where there is difference in one altititude higher than current altitude
            - the end of a hiking trail is at a 9
            - so you need to traverse 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 going left, right, up, or down,
            starting at a 0 for it to be a hiking trail.
Notes:
- it is only left, up, right, down directions for adjacent paths
    - no diagonals
- each trailhead has the possiblity of reaching any 9
    - just because one trail head reaches a 9, doesn't mean another trailhead cant. You would count this
    as 1 for both trail heads.
- a trailhead can reach the same 9 by two different trails, but this only counts as one point
Approach:
- Do a BFS from somewhere?
    - one option is to do it starting at every 0 and look for 9s
        - if we go with this option, we might end up doing more operations:
            - many paths will strart from 0 and increase, and never reach a 9, nvm we dont know this
    - anothe option is to do it at every 9 and look for 0s
        - I think this option makes more sense since one 9 can have multiple trailheads and 
        we want to count each of its trail heads as a point.
    - nevermind, lets just go with the 0 way, its how the problem lays it out, and im pretty sure its just as efficient
    - each 0 will need to run its own search since every 9 is fair game for each 0
Algorithm:
- create grid of map
- define result
- Run BFS or DFS on each 0 following:
    - define set of 9s for each trailhead
    - define variable for trailhead score
    - adjacent node is up, down, left, or right and one altitude higher than current altitude
    - once a 9 is encountered, save its location in a set
        - if the 9 isn't in the set already, increase the trailheads score by 1
- sum up all of the trailhead scores into result and return
- Time: O(n^2) -> every node will run a traversal
- Space: O(n) -> visited set

How to do a graph traversal?
- Create a deque: queue (BFS) or stack (DFS) for storing nodes
    - store first node (trailhead)
- while you have node in deque
    - pop node
    - if the node is not in visited
        - add it to visited
        - loop through all directions
            - add each valid adjacent node to deque of traversable nodes
- in our case, also create a 9s set and populate this set whenever a 9 is traversed in the traversal
Things I decided on while coding:
- just use ASCII values instead of converting to int
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
    visited = set()
    trailEnds = set()

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            r, c = node
            alt = ord(trailMap[r][c])

            if alt == 57:
                trailEnds.add((r, c))
            else:
                for dR, dC in directions:
                    newR = r + dR
                    newC = c + dC

                    if newR in range(numR) and newC in range(numC):
                        newAlt = ord(trailMap[newR][newC])
                        if newAlt > 46 and newAlt == alt + 1:
                            queue.append((newR, newC))

    return len(trailEnds)

            



for r in range(numR):
    for c in range(numC):
        if trailMap[r][c] == "0":
            result += getTrailHeadScore(r, c)

print(result)