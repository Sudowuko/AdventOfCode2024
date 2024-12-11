"""
Update:
- 75 blinks instead of 25
- already tried, this is taking extremely long
Change:
- Think i need to update the rules
    - i.e. if you encounter a 0 -> 1 -> 2024 -> 20 24 -> 2 0 2 4 -> 4048 1 4048 8096 -> 40 48 2024 40 48 80 96 -> 4 0 4 8 20 24 4 0 4 8 8 0 9 6
- Order ddoesn't actually matter since we are just counting stones
- Once you get an even digit number, it will continue splitting until there are only single digits
    - if you know what happens to 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, you can already calculate what each stone would turn into?
    - so for every even digit number, it will take numDigits // 2 blinks to get to single numbers
        - we could save computation by not splitting the even digit node up until numDigits // 2 blinks are reached

- 36869184 -> 3686 9184 -> 36 86 91 84 -> 3 6 8 6 9 1 8 4
        

- 0 -> -> * -> 2 blinks
- 1 -> * -> 2 blinks
- 2 -> * -> 2 blinks
- 3 -> * -> 2 blinks
- 4 -> * -> 2 blinks
- 5 -> -> * -> 3 blinks
- 6 -> -> * -> 3 blinks
- 7 -> -> * -> 3 blinks
- 8 -> -> * -> 3 blinks
- 9 -> -> * -> 3 blinks

before I go eat:
    - On non-even digit numbers:
        - just multiply unitl even
    - on even digit numbers:
        - keep stone count and update on every blink
        - once you have reached all single digit stones (after x amount of blinks)
            - create the new stones?
Does this actually improve time?:
- if you have one stone: 5
    - u will be able to go through 4 blinks almost instantly
    - then the last blink is where you create the nodes
    - but you are still creating x amount of nodes, you are still creating the same amount
- at most, a single digit stone will take 5 blinks before creating more single digits stones
- i am also no longer splitting values of nodes and all that
    - technically my first solution would have more nodes present than my current solution
    - maybe this is already good enough?

Updated Algorithm:
- Create a map for every single digit
    - key: digit
    - value will be [number of blinks while at one stone, max num blinks, [digits once even]
- Create initial linked list
    - Define node as:
        - value
        - num blinks
        - max num blinks
        - next
- Run the for loop for 75 times
    - handle nodes as normal
    - if node digits are not even and not in map:
        - multiply by 2024
    - if node digits are even:
        - max num blinks is total number of digits // 2
        - if max num blinks is reached:
            - create node for each digit
                - num blinks start at 0
        - else:
            - increment num blinks by 1
    - else:
            num blinks += 1
            - if max numb blinks is reached
                - create node for every digit in digits
                - num blinks starts at 0

for every node in linked list: * Should all be digits at this point
    - if num blinks <= number of blinks while at one stone -> stone count is 1
    - if numb blinks > number of blinks while at one stone -> (num blinks - number of blinks while at one stone)

"""

class Node:
    def __init__(self, val=""):
        self.val = val
        self.numBlinks = 0
        if val in dMap:
            self.maxNumBlinks = dMap[val][1]
        else:
            self.maxNumBlinks = len(val) // 2
        self.next = None

dMap = {
    "0": [2, 5, [2, 0, 2, 4]],
    "1": [1, 3, [2, 0, 2, 4]],
    "2": [1, 3, [4, 0, 4, 8]],
    "3": [1, 3, [6, 0, 7, 2]],
    "4": [1, 3, [8, 0, 9, 6]],
    "5": [2, 5, [2, 0, 4, 8, 2, 8, 8, 0]],
    "6": [2, 5, [2, 4, 5, 7, 9, 4, 5, 6]],
    "7": [2, 5, [2, 4, 5, 7, 9, 4, 5, 6]],
    "8": [2, 5, [2, 8, 6, 7, 6, 0, 3, 2]],
    "9": [2, 5, [3, 6, 8, 6, 9, 1, 8, 4]]
}


#Creates singly linked list
dummy = Node("0")

with open('11_input.txt', 'r') as file:
    for line in file:
        stones = line.split(" ")
        prevNode = None
        print(stones)
        for stone in stones:
            newNode = Node(stone)
            if prevNode:
                prevNode.next = newNode
            else:
                dummy.next = newNode
            prevNode = newNode

for i in range(75):
    print(i)
    currNode = dummy.next
    prevNode = dummy

    while currNode: 
        val = currNode.val
        if val in dMap:
            currNode.numBlinks += 1
            # print(currNode.numBlinks, currNode.maxNumBlinks)
            if currNode.numBlinks == currNode.maxNumBlinks:
                oldCurr = currNode
                for digit in dMap[val][2]:
                    currNode = Node(str(digit))
                    prevNode.next = currNode
                    prevNode = currNode
                currNode.next = oldCurr.next
                del oldCurr
        else:
            numDigits = len(val)
            if numDigits % 2 == 0:
                currNode.numBlinks += 1
                if currNode.numBlinks == currNode.maxNumBlinks:
                    oldCurr = currNode
                    for i, digit in enumerate(val):
                        if i == 3:
                            continue
                        currNode = Node(str(digit))
                        prevNode.next = currNode
                        prevNode = currNode
                    currNode.next = oldCurr.next
                    del oldCurr
            else:
                currNode.val = str(int(val) * 2024)

        prevNode = currNode
        currNode = currNode.next

currNode = dummy.next
numStones = 0
while currNode:
    if currNode.numBlinks <= dMap[currNode.val][0]:
        numStones += 1
    else:
        numStones += 2 * (currNode.numBlinks - dMap[currNode.val][0])
    currNode = currNode.next

print(numStones)

