"""
Input:
- Maze 
- Starting point
- Ending point
Output:
- The lowest score a reindeer could get:
    - moving forward in the current direction your facing gives 1 point
    - turning 90 degrees gives 1000 points
Approach:
- BFS seems hard here because you need to account for the turns as well
    - You could treat a turn as going forward 1000 times but I think that 
    it will end up being really inefficient once the scores get into the millions
    or something
- Dikstra is usually better for solving this case
    - although we dont have edge lengths can we just keep track of score at each node?
    - We can do dikstras, but instead of edge lengths, we keep track of distance using the
    rules in the question
    - We do not need to keep track of path, just distance
- How do you implement Dikstras?
    - Need visited set, need unvisited set, need distance to each node
    - Give every node a distance of inf except for S
    - You can access every adjacent node by using the directions and avoiding walls
        - remember that 90 degree nodes will have a distance of 1001 from current
        - 180 degree nodes will have a distance of 2001 from current
        - 0 degree nodes will have a distance of 1 from current
    - You start at S, update the distance of all adjacent nodes (using the rules
    above)
    - Find the node with the smallest distance in unvisited
    - pop it from unvisited and check its adjacent nodes (and add to visited)
        - update those nodes, and so on
    - once unvisited is empty, you are done
- How should we implement dikstras?
    - Use visited set for coords
    - Use map for mapping coord to distance
    - use unvisited set for coords
    - when checking for minimum, we just loop through unvisited and find minimum
    - also need to keep track of current direction to get distances for each node
        - save this in distances map so that you could access the direction that 
        that node was accessed from to determine points
"""

#Define sets
visited = set()
unvisited = set()
distances = {}

#Create grid
maze = []

with open("16_input.txt", "r") as file:
    for line in file:
        maze.append(list(line[:-1]))

rows = len(maze)
cols = len(maze[0])

end = (None, None)
start = (None, None)

for r in range(rows):
    for c in range(cols):
        node = maze[r][c]
        if node == "#":
            continue
        elif node == "S":
            start = (r, c)
            maze[r][c] = "."
        elif node == "E":
            end = (r, c)
            maze[r][c] = "."
           
        unvisited.add((r, c))

for node in unvisited:
    distances[node] = [float('inf'), None] #Second index is direction

distances[start][0] = 0
distances[start][1]  = "E"

currDir = "E"

directions = {
    (0, 1): "E",
    (-1, 0): "N",
    (1, 0): "S",
    (0, -1): "W",
}

dir90s = {
    "E": {"N", "S"},
    "W": {"N", "S"},
    "S": {"E", "W"},
    "N": {"E", "W"}

}

#Now do dikstras
while unvisited:
    #Find minimum distance node
    minNode = (None, None)
    minDistance = float('inf')
    for node in unvisited:
        if distances[node][0] <= minDistance:
            minNode = node
            minDistance = distances[node][0]
    
    # visited.add(minNode)
    unvisited.remove(minNode)

    incomingDir = distances[minNode][1]
    incomingDist = distances[minNode][0]

    currR = minNode[0]
    currC = minNode[1]

    #Update distances of nodes adjacent to minNode and keep track of direction
    for direction, symbol in directions.items():
        newR = currR + direction[0]
        newC = currC + direction[1]

        if newR not in range(rows) or newC not in range(cols) or maze[newR][newC] != ".":
            continue

        newDist = None

        if symbol in dir90s[incomingDir]:
            newDist = incomingDist + 1001
        elif symbol == incomingDir:
            newDist = incomingDist + 1
        else:
            continue

        if newDist < distances[(newR, newC)][0]:
            distances[(newR, newC)] = [newDist, symbol]

print(distances[end])

currNode = end

while currNode != start:
    r = currNode[0]
    c = currNode[1]

    maze[r][c] = "O"

    incomingDir = distances[currNode][1]

    if incomingDir == "N":
        currNode = (currNode[0] + 1, currNode[1])
    elif incomingDir == "S":
        currNode = (currNode[0] - 1, currNode[1])
    elif incomingDir == "E":
        currNode = (currNode[0], currNode[1] - 1)
    else:
        currNode = (currNode[0], currNode[1] + 1)

for line in maze:
    print("".join(line))

