"""
Input:
- line of stones
    - each stone has a number
Output:
- Whare are the stones present once you blink 25 times
    - on each blink a set of rules are applied to each stone changing them or creating new stones
Notes:
- stones are always placed along a straight line, with order being preserved
    - stones cannot hop over other stones
- rules apply to single stones only
- any leading 0s on new stones are cut off
Approach:
- Maybe use a linked list?
    - Updating value would be easy
    - creating two nodes to replace current node would be easy
    - going to next node depending on rule would be easy
    - would help with time complexity since adding nodes would be constant time
        - you are always only adding nodes at the given point location (replace current pointer with two)
- If we were to use an array, in would be a bit more annoying to handling the indices and pointers to them
    - adding elements would also require a shifting of every other element, making time complexity worse
- go with linked list

Steps:
- Define Node class
- Convert input into a singly linked list
- run a for loop 25 times:
    - set currNode to head of linked list
    - set prevNode to None (prevNode is needed for rule 2)
    - while currNode:
        - apply rule on current node
        - if rule 1 or 3, just update current node val
        - if rule 2, create two new nodes (applying notes) and handle next and prev node pointers
- get length of linked list
- return length
- Time: O(25*n + n) -> O(n), Space: O(n)

If we were doing array:
- Time: O(25*n^2) -> assuming that rule 2 is used A LOT (shifting a lot of vals), Space: O(n)
Things I noticed while coding:
- doubly linked list would make it so that we do not actually need two pointers
    - also might be good for part 2 depending on what it is
- nvm lets just make this change later
- Use dummynode so u dont need to keep track of head all the time
"""

class Node:
    def __init__(self, val="", next=None):
        self.val = val
        self.next = next


#Creates singly linked list
dummy = Node()

with open('11_input.txt', 'r') as file:
    for line in file:
        stones = line.split(" ")
        prevNode = None
        for stone in stones:
            newNode = Node(stone)
            if prevNode:
                prevNode.next = newNode
            else:
                dummy.next = newNode
            prevNode = newNode

for i in range(25):
    print(i)
    currNode = dummy.next
    prevNode = dummy

    while currNode:
        val = currNode.val
        if val == "0":
            currNode.val = "1"
        elif len(val) % 2 == 0:
            firstHalf = val[:len(val) // 2]
            secondHalf = val[len(val) // 2:]

            #Strip leading 0s
            secondHalf = secondHalf.lstrip("0") or "0"

            newNode = Node(firstHalf)
            prevNode.next = newNode
            newNode.next = currNode
            currNode.val = secondHalf
        else:
            currNode.val = str(int(val) * 2024)

        prevNode = currNode
        currNode = currNode.next

currNode = dummy.next
numStones = 0
while currNode:
    # print(currNode.val, end=" ")
    numStones += 1
    currNode = currNode.next

print(numStones)

