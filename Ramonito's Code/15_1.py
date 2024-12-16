"""
Input:
- Map
- List of robot movements
Output:
- Sum of all GPS coordinates for each box after all of the robot movements
    - Robot movement rules:
        - If the robot runs into a box, it will try to move that box
            - The robot can no longer move a box if it is touching
            a chain of boxes that are already touching a wall of the map (#)
                - Walls exist within the map, not just on edges
            - a robot also cannot move a #
Approach:
- What are the cases we run into?
    - Run into a #:
        - do not move 
    - Run into a O:
        - O is in front of other Os
            - Find end of Os: -> prob use while loop for this
                - if end of Os is a ., remove immediate O and add O on .
                - if end of Os is a #, dont move
        - O is in front of #
            - dont move
        - O is in front of .
            - remove immediate O, place O at .
    - Run into a .:
        - move in that direction
- Efficieny:
    - All operations are constant time except when there are multiple Os blocking the movement
        - worst case, we would need to view an entire row or col at every movement
Algorithm:
- Convert map into grid
- Take note of initial position
- Loop through every movement:
    - Remeber to ignore "\n" characters
    - Define a direction for each movement character: Can use hash map for this
    - Depending on movement character:
        - Check for each of the cases outlined above
            - If the Os in front of other Os case
                - Keep track of a pointer
                - Update pointer until it no longer points to an O
                - Update grid locations accordingly
"""

dirMap = {
    "<": [0, -1],
    ">": [0, 1],
    "^": [-1, 0],
    "v": [1, 0]
}

with open("15_input.txt", "r") as file:
    grid = []
    numR = 0
    numC = 0
    currR = 0
    currC = 0

    for line in file:
        if line[0] == "#":
            grid.append(list(line[:-1]))
        elif line[0] == "\n":
            numR = len(grid)
            numC = len(grid[0])

            for r in range(numR):
                for c in range(numC):
                    if grid[r][c] == "@":
                        currR = r
                        currC = c
                        grid[r][c] = "."
        elif line[0] != "\n":
            for move in line[:-1]:
                dR, dC = dirMap[move]
                newR = currR + dR
                newC = currC + dC

                nextTile = grid[newR][newC]

                if nextTile == "#":
                    continue
                elif nextTile == ".":
                    grid[currR][currC] = "."
                    currR = newR
                    currC = newC
                else:
                    while nextTile == "O":
                        newR += dR
                        newC += dC
                        nextTile = grid[newR][newC]
                    
                    if nextTile == ".":
                        grid[currR + dR][currC + dC] = "."
                        grid[newR][newC] = "O"
                        currR += dR
                        currC += dC
                    else:
                        continue

    for line in grid:
        print("".join(line))

    result = 0

    for r in range(numR):
        for c in range(numC):
            if grid[r][c] == "O":
                result += 100 * r + c
    
    print(result)


