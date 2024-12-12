"""
Input:
- garden plot with different regions
    - each region is indicated by a group of capital letters
Output:
- price of fencing all regions in the map
    - price of fencing for one region is the perimeter * the area of a region
    - the area of a region is the total number of garden plots the region contains
    - the perimeter of a region is the number of sides of garden plots in te region that do not touch another garden
Approach:
- Graph traversal makes the most sense:
    - We can view all regions as disconnected graphs
    - for each garden plot:
        - traverse its region (traverse garden plots of same region)
        - to keep track of area, if garden plot is added to traversal queue, increase area by 1
        - to keep track of perimeter, for every side of the garden plot that is not added to queue, 
        increase perimeter by 1
    - once a queue is empty (all garden plots have been traversed for that region), calculate cost and add to result
    - since we have a visited set for the entire garden, regions that are traversed will not be traversed again
    - Time: O(V + E), Space: O(V)
"""

from collections import deque

garden = []
price = 0

#Convert input into grid
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
    perimeter = 0
    stack = deque()
    stack.append((initR, initC))

    while stack:
        gardenPlot = stack.pop()
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
                    perimeter += 1

    # print(perimeter, area)
    return perimeter * area

for r in range(numR):
    for c in range(numC):
        if (r, c) not in visited:
            price += getPrice(r, c)

print(price)
