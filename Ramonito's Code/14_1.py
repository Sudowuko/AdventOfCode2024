"""
Input:
- List of robot positions and their respective velocities

Output:
- We want the final positions of all robots after 100 seconds
- With these final positions, we count how many robots are in each quadrant
    - any robots directly along the middle of between each quadrant are not considered
- The map dimensions are 101 tiles wide and 103 tiles tall
    - so the row that doesn't count is row 52
    - the col that doesn't count is col 51 (be careful with 0 indexing)
- with the number of robots in each quadrant, we multiply them together and that is our answer

Notes:
- Multiple robots can be on a single tile (means that we can handle each robot separately
and still get the same answer by the end)
- When a robot reaches an edge, they wrap around the current edge they cross
    - i.e .....1. + 2 in -> = 1......
- Timed problem
    - meaning brute force method probably wont suffice for larger input

Ideas:
- We could just do this iteratively for each robot
    - Apply velocity at starting position with wrapping rules when reaching edges
    - Once all robots have move for 100 seconds, we count the number of robots in each quadrant
    - Since this is brute force, I do not think that it will pass for part 2
- Math approach again?
    - It does not matter which direction you move in first when handling a displacement
        - If velocity and time are known in one direction, we can just calculate displacement right away
            - hard part is handling the wrapping mathematically
            - if we have 1.... and displacement is 7 we get ..1..
                - displacement was actually 2
                    - therefore real displacement is displacement % total area + original position?
                    - how about .1... and displacement is 7 we get ...1. -> so it still works yea
                    - how about ....1 ? .1...
                        - so if remainder is greater than total width, get remainder of that and width as displacement
Algorithm:
- Create variables for storing quantity of each quadrant
    - for each robot:
        - handle x direction first
            - get totalDisp by doing vel * time
            - get actualDisp by doing 101 % totalDisp
            - if if actualDisp + originalPos > 101
            - finalDisp is (originalPos + actualDisp) % 101
        - handle y direction with 103 instead of 101 and the y values for velocity and position
        - with the new position, check which quadrant ur in and update the correct variable
- Time: O(n * time) -> This is a constant operation for each robot

Corner Cases while coding:
- Negative numbers were not being handled correctly
    - .1..., -7 ->
    - fix: just made length negative when working with negative displacement
        - Update logic accoridngly
        - 1##... from .1. -> went from 2 to -3 so 
- Also realized that nothing will every have a displacement of 0
Lesson:
- When working with math. Once there is a math mistake with ur code, ur better off just rewriting
the math parts than trying to tweak the one off errors ( you might change more than you need )
"""

#Define result
q1Count = q2Count = q3Count = q4Count = 0
width = 101
height = 103

#For debugging
grid = []
for i in range (height):
    grid.append(["."] * width)

#Define dispCalc
def calcDisp(time, length, p, v):
    # totalDisp = v * time
    # if totalDisp < 0:
    #     actualDisp = totalDisp % -length
    # else:
    #     actualDisp = totalDisp % length
    

    # updatedPos = p + actualDisp

    # print(p, v, length, updatedPos)
 
    # if updatedPos >= length:
    #     return updatedPos % length
    # elif updatedPos < 0:
    #     return length + updatedPos - 1
    # return updatedPos

    totalDisp = v * time

    dispAfterCycles = totalDisp % length

    updatedPos = p + dispAfterCycles

    if updatedPos > length - 1:
        cycledPos = updatedPos - length
        return cycledPos
    elif updatedPos < 0:
        cycledPos = length - updatedPos
        return cycledPos
    
    return updatedPos

for time in range(100,89, -1):
    grid = []
    for i in range (height):
        grid.append([" "] * width)
    with open("14_input.txt", "r") as file:
        for line in file:
            pos, vel = line[:-1].split()
            px, py = int(pos.split(",")[0].split("=")[1]), int(pos.split(",")[1])
            vx, vy = int(vel.split(",")[0].split("=")[1]), int(vel.split(",")[1])

            newX = calcDisp(time, width, px, vx)
            newY = calcDisp(time, height, py, vy)

            widthBoundary = width // 2 + 1 - 1
            heightBoundary = height // 2 + 1 - 1

            # print(widthBoundary, heightBoundary)

            # if newX not in range(0, width) or newY not in range(0, height):
                # print(py, vy, newY)

            if grid[newY][newX] == " ":
                grid[newY][newX] = 1
            else:
                grid[newY][newX] += 1

            if newX < widthBoundary and newY < heightBoundary:
                q1Count += 1
            elif newX > widthBoundary and newY < heightBoundary:
                q2Count += 1
            elif newX < widthBoundary and newY > heightBoundary:
                q3Count += 1
            elif newX > widthBoundary and newY > heightBoundary:
                q4Count += 1

    for i in range(height):
        for j in range(width):
            grid[i][j] = str(grid[i][j])
    print("")
    print("")
    print("")
    print("TIME------------------------------------------------------------:", time)
    
    for line in grid:
        print("".join(line))

# print(q1Count, q2Count, q3Count, q4Count)
print(q1Count * q2Count * q3Count * q4Count)
