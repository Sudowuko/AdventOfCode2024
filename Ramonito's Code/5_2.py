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
"""

from collections import defaultdict

#Define variables
rules = defaultdict(set)
result = 0

#Define line function
def calcLine(updates):
    for i, update in enumerate(updates):
        for j in range(i):
            if updates[j] in rules[update]:
                return 0
    
    return updates[len(updates) // 2]

with open('5_input.txt', 'r') as file:
    breakIndex = 0
    for i, line in enumerate(file):
        if i == breakIndex:
            rule = line[:-1].split("|")
            if len(rule) == 2:
                rules[rule[0]].add(rule[1])
                breakIndex = i + 1
        else:
            updates = line[:-1].split(",")
            result += int(calcLine(updates))

print(result)


