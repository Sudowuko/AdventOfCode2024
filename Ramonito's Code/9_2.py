"""
Update:
- instead of moving pieces of memory 1 by 1, we want to move contigous blocks of memory with the same ID
- On each new memory block, you want to start looking agian from the left of the space
Change:
- Could maybe use a map store indices of the starting point for free spaces of different lengths, but its kinda a lot
- On every contigous block encountered, just look from left to right until you find space it fits
New Algorithm:
- Have two pointers still
- While loop until right pointer goes through all IDs
    - loop until right pointer finds id
        - used a temp pointer to count how long this block of memory is for this id
    - while loop until left pointer passes temp pointer or slot found or left reaches end
        - increament left until it finds a "." or reaches temp pointer
        - use left temp pointer to count how long "." section is
            - once you reach the length of the block
            - use two left pointers to fill in this space with block values and temp and right to erase memory at block
            - use flag to indicate that slot has been found
        
Corner Cases:
- I think I need to create a set of moved Ids so that I do not run into them again and keep on going
        
"""

space = []
movedIds = set()
currId = None

with open('9_input.txt', 'r') as file:
    for line in file:
        line = list(line)
        id = 0
        for i, memory in enumerate(line):
            if i % 2 == 0:
                for i in range(int(memory)):
                    space.append(str(id))
                id += 1
            else:
                for i in range(int(memory)):
                    space.append(".")
right = len(space) - 1

while right >= 0:
    print(right)
    while right >= 0 and space[right] == "." or space[right] in movedIds:
        right -= 1

    if right < 0:
        break
    currId = space[right]
    if currId in movedIds:
        continue
    tempRight = right
    while space[tempRight] == currId:
        tempRight -= 1
    lenBlock = right - tempRight

    # print(lenBlock, right, tempRight, currId)

    left = 0
    slotFound = False
    while not slotFound and left < tempRight:
        while left < len(space) and space[left] != ".":
            left += 1

        if left > tempRight: break

        tempLeft = left
        while space[tempLeft] == ".":
            if tempLeft - left + 1 == lenBlock:
                for i in range(tempLeft, left - 1, -1):
                    space[i] = currId
                for i in range(tempRight + 1, right + 1):
                    space[i] = "."
                slotFound = True
                movedIds.add(currId)
            tempLeft += 1

        while left < len(space) and space[left] == ".":
            left += 1
    right = tempRight
    # print(left, tempRight, right, space[tempRight])
        


checksum = 0

for i, id in enumerate(space):
    if id != ".":
        checksum += i * int(id)

# print("".join(space))
print(checksum)
