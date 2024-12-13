def TurnRight(input):
    if input == 270:
        return 0
    else:
        return (input + 90)

def GetDirection(input):
    if input == 0:
        return "UP"
    elif input == 90:
        return "RIGHT"
    elif input == 180:
        return "DOWN"
    else:
        return "LEFT"

def CheckNext(output, direction, row, col, item):
    if direction == "UP":
        if output[row - 1][col] == item:
            return True
    elif direction == "RIGHT":
        if output[row][col + 1] == item:
            return True
    elif direction == "DOWN":
        if output[row + 1][col] == item:
            return True
    elif direction == "LEFT":
        if output[row][col - 1] == item:
            return True
    else:
        return False

def CheckCurrent(output, row, col, item):
    if output[row][col] == item:
        return 1
    else:
        return 0
        

def GuardRoute():
    f = open("6_input.txt", "r")
    input  = f.read().splitlines()

    output = []
    report = []
    for x in input:
        for y in x:
            report.append(y)
        output.append(report)
        report = []
    
    # To find the guard position
    pos_guard = {}
    for pos_x, x in enumerate(output):
        for pos_y, y in enumerate(x):
            if y == "^":
                pos_guard = {"row": pos_x, "col": pos_y}
                output[pos_x][pos_y] = "X"
    distinct_count = 1
    direction = "UP"
    direction_num = 0
    row_count = len(output)
    column_count = len(output[0])
    while (True):
        row = pos_guard["row"]
        col = pos_guard["col"]
        #Check if guard exits array
        if (direction == "UP"):
            if pos_guard["row"] - 1 < 0:
                distinct_count += CheckCurrent(output, row, col, ".")
                break   
        elif (direction == "DOWN"):
            if pos_guard["row"] + 1 >= row_count:
                distinct_count += CheckCurrent(output, row, col, ".")
                break
        elif (direction == "RIGHT"):
            if pos_guard["col"] + 1 >= column_count:
                distinct_count += CheckCurrent(output, row, col, ".")
                break
        elif (direction == "LEFT"):
            if pos_guard["col"] - 1 < 0:
                distinct_count += CheckCurrent(output, row, col, ".")
                break
        # Check if you encounter a wall
        if CheckNext(output, direction, row, col, "#"):
            direction_num = TurnRight(direction_num)
            direction = GetDirection(direction_num)
        # Check if you're on a dot tile
        if output[row][col] == ".":
            distinct_count += 1
            output[row][col] = "X"
        # Continue on the same path based on direction
        if (direction == "UP"):
            pos_guard["row"] -= 1
        elif (direction == "RIGHT"):
            pos_guard["col"] += 1
        elif (direction == "DOWN"):
            pos_guard["row"] += 1
        elif (direction == "LEFT"):
            pos_guard["col"] -= 1
        #Traverse
    print("Distinct Count: ", distinct_count)

GuardRoute()

# ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'], 
# ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '#'], 
# ['.', '.', '.', '.', 'X', '.', '.', '.', 'X', '.'], 
# ['.', '.', '#', '.', 'X', '.', '.', '.', 'X', '.'], 
# ['.', '.', 'X', 'X', 'X', 'X', 'X', '#', 'X', '.'],
# ['.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'],
# ['.', '#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
# ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '#', '.'], 
# ['#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'], 
# ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']