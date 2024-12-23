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
Corner Cases?:
- Answer works on given input but not actual
- dikstras should work if the graph edges never change value, and there are no negative cycles
- my guess it that since i am treating the spots as nodes and their connection to to other spots
as edges, its clear that a specific edge can and will change values depending on which direction you
entered in on. 
    - just an idea, but i feel like the changing edge values are not captured well in dikstras
    - so intead, what if we create 4 nodes for each spot on the maze. 
        - one node representing entering the spot from each possible direction. This way, the edge values 
        no longer change.
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

dirOps = {
    "E": "W",
    "N": "S",
    "W": "E",
    "S": "N",
}


for r in range(rows):
    for c in range(cols):
        node = maze[r][c]
        if node == "#":
            continue
        elif node == "S":
            start = (r, c)
            maze[r][c] = "."
            unvisited.add(((r, c), "E"))
        elif node == "E":
            end = (r, c)
            maze[r][c] = "."
        
        for dir, sym in directions.items():
            newR = r + dir[0]
            newC = c + dir[1]
            if (r, c) == (1, 15):
                print("dirOPS", sym, maze[newR][newC])

            if newR in range(rows) and newC in range(cols) and (maze[newR][newC] == "." or maze[newR][newC] == "E" or maze[newR][newC] == "S"):
                unvisited.add(((r, c), dirOps[sym]))

for node in unvisited:
    if node[0] == (1, 15):
        print(node)
    distances[node] = float('inf') #Second index is direction

# print(distances)

distances[(start, "E")] = 0

print(end)
#Now do dikstras
while unvisited:
    print(len(unvisited))
    #Find minimum distance node
    minNode = (None, None)
    minDistance = float('inf')
    for node in unvisited:
        if distances[node] < minDistance:
            minNode = node
            minDistance = distances[node]

    if minNode == (None, None):
        break
    
    # visited.add(minNode)
    unvisited.remove(minNode)

    incomingDir = minNode[1]
    incomingDist = distances[minNode]

    currR = minNode[0][0]
    currC = minNode[0][1]

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

        # if minNode[0] == (15, 1):
        # print(minNode[0], incomingDir, incomingDist, newDist, symbol)

        if newDist <= distances[((newR, newC), symbol)]:
            distances[((newR, newC), symbol)] = newDist
            # #Test adding these back in as edge values can technically change depending on path
            # unvisited.add((newR, newC))
            # # unvisited.add((currR, currC))

print(distances[(end, "E")])

currNode = end

# for r in range(rows):
#     for c in range(cols):
#         currNode = (r, c)
#         if currNode == end:
#             print("FOUND END", end)
#         while currNode in distances and currNode != start:
#             # if distances[currNode][1] is None:
#             #     continue
#             r = currNode[0]
#             c = currNode[1]

#             maze[r][c] = "@" #distances[currNode][1]#str(round(distances[currNode][0] / 7036, 1))

#             incomingDir = distances[currNode][1]

#             if incomingDir == "N":
#                 currNode = (currNode[0] + 1, currNode[1])
#             elif incomingDir == "S":
#                 currNode = (currNode[0] - 1, currNode[1])
#             elif incomingDir == "E":
#                 currNode = (currNode[0], currNode[1] - 1)
#             else:
#                 currNode = (currNode[0], currNode[1] + 1)

# for r, c in distances.keys():
#     if distances[(r, c)][0] < 50000:
#         maze[r][c] = "@"

for line in maze:
    print("".join(line))

