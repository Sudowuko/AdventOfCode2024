"""
Update:
- want to sort values so that they follow the rules correctly
- to follow the rule, no values before current value should be in rules array
Examples:
- [61, 13, 29], 29|13
    - you would swap 29 and 13
- [10, 12, 61, 45, 50], 45|61, 50|61, 61|10, 61|12
    - [12, 61, 10, 45, 50]
    - [61, 12, 10, 45, 50]
    - []
Notes:
- Realized that simply swapping or moving things before and after values wont work in certain cases
- I think that I could maybe use a tree of some sort to do this
    - What if you make a tree where each parent node must come before its child nodes
- What if you use a graph of some sort -> topological sort thing
    - Are we garaunteed that this is an acyclic graph?
- What if we create a head node that points to all nodes at first
    - then as we go through the rules a second time
        - for every node in a nodes rule set, we make it a child of that node
        - assuming there are no cycles possible, we can then start at the top of the tree and do a level traversal
- Gonna try drawing it
    - If you are getting the middle number in the corrected update list, that means the middle number will always be unique
    - Means that 13 will always be at end
Next Day Notes:
- If the middle number in any update will always be unique, it means that there can never be a cycle within a list of updates
    - Upon drawing I found the graph to be very cyclic, but this will cause problems in updates that should be sorted
    - Therefore, I am assuming that any list of updates will never have a cycle
        - from this information, instead of making the graph or something out of all of the rules, just make it for the specific
        update list using the rules, then you should be able to topologically sort (dont remember how to do that) -> check notes
        - You can use topological sort on this because in order for the graph to be sortable, it must be acyclic and directional
        - You cant topological sort the entire rule set because there are cycles, but if they are saying that the wrong updates should
        be sortable, that means that by definition there cant be a cycle, since the list would always contradict itself
            - and since there cant be a cycle, it is acyclic -> topological sort if possible
Algorithm:
- Define topological sort algorithm
- Create rule map
- for every node in list, check with every other node
    - if node is in set of current node in hash map, create dependency tuple, and add to list of edges
    - also add current node to list of nodes -> should be unique for given problem
- Run topological sort, on given node list and edges
- return order
- get middle value in returned order
- increment result with middle value
Things I ran into during coding:
- Only want to calculate mid vals of corrected incorrect updates
"""

from collections import defaultdict

def graph_topo_sort(nodes, edges):
    from collections import deque
    nodeMap, orderedNodes, queue = {}, [], deque()
    for node in nodes:
        nodeMap[node] = { 'in': 0, 'out': set() }
    for node, preNode in edges:
        nodeMap[node]['in'] += 1
        nodeMap[preNode]['out'].add(node)
    for node in nodes:
        if nodeMap[node]['in'] == 0:
            queue.append(node)
    while len(queue):
        node = queue.pop()
        for outgoingNode in nodeMap[node]['out']:
            nodeMap[outgoingNode]['in'] -= 1
            if nodeMap[outgoingNode]['in'] == 0:
                queue.append(outgoingNode)
        orderedNodes.append(node)
    return orderedNodes if len(orderedNodes) == len(nodes) else None

#Define variables
rules = defaultdict(set)
result = 0

#Define line function
def calcLine(updates):
    for i, update in enumerate(updates):
        for j in range(i):
            if updates[j] in rules[update]:
                return -1
    
    return updates[len(updates) // 2]

def createEdges(updates, rules):
    edges = []
    for currNode in updates:
        for possibleDependantNode in updates:
            if possibleDependantNode in rules[currNode]:
                edges.append((possibleDependantNode, currNode))
    return edges

with open('5_input.txt', 'r') as file:
    breakIndex = 0
    for i, line in enumerate(file):
        #Rule map creation
        if i == breakIndex:
            rule = line[:-1].split("|")
            if len(rule) == 2:
                rules[rule[0]].add(rule[1])
                breakIndex = i + 1
        #Update list handling
        else:
            updates = line[:-1].split(",")
            midVal = int(calcLine(updates))

            if midVal < 0:
                edges = createEdges(updates, rules)
                sortedUpdates = graph_topo_sort(updates, edges)
                midVal = int(sortedUpdates[len(sortedUpdates) // 2])
                result += midVal

print(result)


