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
- I think we can just handle it node by node
    - in this case we would just store the prev of a node to be when it is the smallest or equal to the smallest distance
Many Corner Cases:
- Could not just store previous for a given node since you that would not be my original dikstras algoirhtm
- was updating distance before checking prev, so prevs were not updating correctly
"""

from collections import deque

#Define sets
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
        
        for dir, sym in directions.items():
            newR = r + dir[0]
            newC = c + dir[1]
            if newR in range(rows) and newC in range(cols) and maze[newR][newC] != "#":
                unvisited.add(((r, c), dirOps[sym]))

for node in unvisited:
    distances[node] = float('inf') #Second index is direction
    prevs[node] = []

distances[(start, "E")] = 0

#Now do dikstras
while unvisited:
    #Find minimum distance node
    minNode = (None, None)
    minDistance = float('inf')
    for node in unvisited:
        if distances[node] < minDistance:
            minNode = node
            minDistance = distances[node]

    if minNode == (None, None):
        break
    
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

        if newDist <= distances[((newR, newC), symbol)]:
            if newDist < distances[((newR, newC), symbol)]:
                prevs[((newR, newC), symbol)] = [minNode]
            else:
                prevs[((newR, newC), symbol)].append(minNode)
            distances[((newR, newC), symbol)] = newDist

seats = set()
seats.add(end)
seatQueue = deque()

#Loop through 4 nodes of end to see which one is best direction to come from
minDist = float('inf')
for dir, symbol in directions.items():
    if (end, symbol) in distances and distances[(end, symbol)] < minDist:
        seatQueue = deque()
        minDist = distances[(end, symbol)]
    
    if (end, symbol) in distances and distances[(end, symbol)] == minDist:
        seatQueue.append((end, symbol))

while seatQueue:
    currSeat = seatQueue.pop()
    for prevNode in prevs[currSeat]:
        if prevNode[0] not in seats:
            seats.add(prevNode[0])
        seatQueue.append(prevNode)

for r, c in seats:
    maze[r][c] = "|"

print(len(seats))
