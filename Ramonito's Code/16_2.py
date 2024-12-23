"""
Update:
- Need to count how many tiles belong to at least one of the best paths in the maze
- Dikstras only keeps track of the shortest distance from the end ot the start
- what we want to do is keep track of all possible paths that lead to this end from the start
- for my input ik that it is only the paths going throuhg end eastwise
- What we need to do is keep track of all paths that work
    - How?
    - Normally, you would access the best path by using a stack to access connected nodes along the path.
        - this would only get you the single best path
    - One thing we could try is going along the path. at every spot in the maze
- What if we jsut store the previous nodes in a list for every node
    - if a previous node got to the same node with the same distance, all nodes stemming from that node are also
    on the best possible path.
- Change:
    - For every node, figure out how to save a list of previous nodes
        - when a node gets to a node and finds the same new distance, we add it to previous
            - basically if it updates or has the same distance, add it to previous
    - starting at the east-wise node going into end, we just use a stack to count its prev nodes up until start
    - use a set so that you do not have duplicates and remove prev from prev list once pushed onto stack so that 
    you do not go in an infinite loop
"""

from collections import deque

#Define sets
visited = set()
unvisited = set()
distances = {}
prevs = {}

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

        prevs[(r, c)] = [[], float('inf')]
        
        for dir, sym in directions.items():
            newR = r + dir[0]
            newC = c + dir[1]

            if newR in range(rows) and newC in range(cols) and (maze[newR][newC] == "." or maze[newR][newC] == "E" or maze[newR][newC] == "S"):
                unvisited.add(((r, c), dirOps[sym]))

for node in unvisited:
    distances[node] = float('inf') #Second index is direction

# print(distances)

distances[(start, "E")] = 0

# print(end)
#Now do dikstras
while unvisited:
    # print(len(unvisited))
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
            if (newR, newC) == end:
                print(newDist, prevs[(newR, newC)][1])
            distances[((newR, newC), symbol)] = newDist
            if newDist < prevs[(newR, newC)][1]:
                prevs[(newR, newC)] = [[(currR, currC)], newDist]

            elif newDist == prevs[(newR, newC)][1]:
                prevs[(newR, newC)][0].append((currR, currC))
            # #Test adding these back in as edge values can technically change depending on path
            # unvisited.add((newR, newC))
            # # unvisited.add((currR, currC))

print(distances[(end, "N")])
print(prevs[end])

currNode = end

seats = set()

seatQueue = deque()
seatQueue.append(end)

while seatQueue:
    currSeat = seatQueue.pop()
    for prev in prevs[currSeat][0]:
        if prev not in seats:
            seats.add(prev)
            seatQueue.append(prev)

for r, c in seats:
    maze[r][c] = "|"

for line in maze:
    print("".join(line))

