"""
Update:
- instead of calculating perimeter, need to calculate number of sides
- new price is number of sides * area

How do we know when we are on a new side?
- Can keep a track of gardenPlots along a side
    - keeping a set of sides that were added to perimeter
        - then, when you are checking a side that would be added to perimeter
        - if there are any adjacent perimeter sides to the one you are looking at
            - do not increase side count
        - if there are no adjacent perimeter sides, this means you have encountered a new side
        - basically, if there is an adjacent perimeter side, you are just accessing an already accounted for side

How do we check adjacent perimeter sides?
- calculate the difference between current garden plot and perimeter side (either col or row should change)
    - if col changes, check the row above and below the perimeter garden plot
    - if row changes, check the col to the right and left of perimeter garden plot
    - in either case if there is at least one other perimeter side that we have accounted for, do not update sides
    - else, update sides by 1
Corner Case while coding:
- Depending on order of traversal, a perimeter side belonging to another side may have been traversed
    - this will stop other sides that use that adjacent perimeter side from being caught
    - to fix, keep track of perimeter side as well as the row or col that it was found from
    - that way sides that are coming from a different similar row or col should still have no adjacent sides
- Depending on order of traversal, a perimeter side may exist for a side, but is more than 1 space away from current side
    - Fix: use BFS instead of DFS
        - you are always traversing nodes that are adjacent to previous nodes before moving on. This gauruntees that 
        a side will be traversed along on direction always, rather than being noticed in one direction, then leaving that direction,
        then coming back from a different direction
    - Other fix: just runa while loop that goes all the way up and all the way down or all the way right or left, and if the region to the left or right or bottom or above
    the garden plot as you are traversing stays the same, and there are no perimeter sides already, you count it as one side.
"""

from collections import deque

garden = []
price = 0

with open("12_input.txt", "r") as file:
    for line in file:
        garden.append(list(line[:-1]))

numR = len(garden)
numC = len(garden[0])

visited = set()
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def getPrice(initR, initC):
    region = garden[initR][initC]
    area = 0
    sides = 0
    perimeterSides = set()
    stack = deque()
    stack.append((initR, initC))

    while stack:
        gardenPlot = stack.popleft()
        if gardenPlot not in visited:
            area += 1
            visited.add(gardenPlot)
            r, c = gardenPlot


            for dR, dC in directions:
                newR = r + dR
                newC = c + dC

                if newR in range(numR) and newC in range(numC) and garden[newR][newC] == region:
                    stack.append((newR, newC))
                else:
                    if newC == c and (newR, newC + 1, r, -1) not in perimeterSides and (newR, newC - 1, r, -1) not in perimeterSides:
                        sides += 1
                    elif newR == r and (newR + 1, newC, -1, c) not in perimeterSides and (newR - 1, newC, -1, c) not in perimeterSides:
                        sides += 1
                    if newC == c:
                        perimeterSides.add((newR, newC, r, -1))
                    elif newR == r:
                        perimeterSides.add((newR, newC, -1, c))

    return sides * area

for r in range(numR):
    for c in range(numC):
        if (r, c) not in visited:
            price += getPrice(r, c)

print(price)
