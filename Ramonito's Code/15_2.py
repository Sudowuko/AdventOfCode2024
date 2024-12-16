"""
Update:
- First need to update map by making all boxes twice as wide -> 
    - "O" becomes "[]"
    - "#" becomes "##"
    - "." becomes ".."
    - "@" becomes "@."
- Boxes can now move more than one adjacent box since guy stays the same size
    - possible change for up down movements:
        - For the obstacle code:
            - Run a recursive function on the box coords trying to find all boxes it will move:
                - This should add the box coords and there box half "[" or "]" to an array
                    - should add both halves to array and run function on both halves
                - To find other boxes that it may move:
                    - run the function on the coord one unit along the current movement direction for each half
                - Base case: coord is a "." -> You can still move -> return True
                - Base case: if coord is an "#" -> you cannot move anything -> Return False

                - at end of function, return all recursive call results "and"ed together
                    - This will ensure that if a "#" is found, you will return False at the first call
            - If recursive run returns True: array is populated with coords of boxes that should move one unit along direction
                - For every coordinate, move box value along direction
                - Update current position of guy
            - If recursive function return False: just continue -> means that there is even just 1 "#" in front of ur boxes so you cant move
    - for left right movements:
        - For obstacle code:
            - store coords and half type in array until you get a "." or "#"
            - if "." loop through array and make the value one unit along the direction of each coordinate equal to the half value
"""

dirMap = {
    "<": [0, -1],
    ">": [0, 1],
    "^": [-1, 0],
    "v": [1, 0]
}


with open("15_input.txt", "r") as file:
    grid = []
    newGrid = []
    numR = 0
    numC = 0
    currR = 0
    currC = 0
    boxes = set()

    def checkMove(grid, boxR, boxC, dR, move):
        tile = grid[boxR][boxC]
        if tile == ".":
            return True
        elif tile == "#":
            return False
        else:
            if tile == "[":
                boxes.add((boxR, boxC, tile))
                boxes.add((boxR, boxC + 1, "]"))
                
                return checkMove(grid, boxR + dR, boxC, dR, move) and checkMove(grid, boxR + dR, boxC + 1, dR, move)
            elif tile == "]":
                boxes.add((boxR, boxC, tile))
                boxes.add((boxR, boxC - 1, "["))
                return checkMove(grid, boxR + dR, boxC, dR, move) and checkMove(grid, boxR + dR, boxC - 1, dR, move)

    for line in file:
        if line[0] == "#":
            grid.append(list(line[:-1]))
        elif line[0] == "\n":
            numR = len(grid)
            numC = len(grid[0])

            #Loop through grid and update items:
            for r in range(numR):
                newGrid.append([])
                for c in range(numC):
                    if grid[r][c] == ".":
                        newGrid[r].extend([".", "."])
                    elif grid[r][c] == "#":
                        newGrid[r].extend(["#", "#"])
                    elif grid[r][c] == "O":
                        newGrid[r].extend(["[", "]"])
                    else:
                        newGrid[r].extend(["@", "."])

            numR = len(newGrid)
            numC = len(newGrid[0])
            
            for r in range(numR):
                for c in range(numC):
                    if newGrid[r][c] == "@":
                        currR = r
                        currC = c
                        newGrid[r][c] = "."
            
            grid = newGrid

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
                    if move in ("<", ">"):
                        boxes = []
                        while nextTile in ("[", "]"):
                            boxes.append((newR, newC, nextTile))
                            newR += dR
                            newC += dC
                            nextTile = grid[newR][newC]
                        
                        if nextTile == ".":
                            currR += dR
                            currC += dC
                            grid[currR][currC] = "."
                            for boxR, boxC, boxHalf in boxes:
                                grid[boxR + dR][boxC + dC] = boxHalf
                        else:
                            continue
                    else:
                        boxes = set()
                        canMove = checkMove(grid, newR, newC, dR, move)

                        if canMove:
                            currR += dR
                            currC += dC
                            grid[currR][currC] = "."
                            for boxR, boxC, boxHalf in boxes:
                                grid[boxR][boxC] = "."
                            for boxR, boxC, boxHalf in boxes:
                                grid[boxR + dR][boxC] = boxHalf

    for line in grid:
        print("".join(line))

    result = 0
    for r in range(numR):
        for c in range(numC):
            if grid[r][c] == "[":
                result += 100 * r + c
    
    print(result)


