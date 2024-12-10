"""
Input:
- HUGE string
    - format is as follows:
        - alternating between space taken up by a block, free space
        - each block as an ID starting at 0 for the most left block and adding 1 on each new block
Output:
- Want to rearrange blocks from right to left and filling up any free space from left to right
- After doing this, we want to return the check sum
    - multiply the index by the ID of the block at that index
Approach:
- Create current space map
    - Alternating between block and free spave
        - recreate input and replace block with block id and free space with "."
        - to alternate, if index % 2 == 0, it is a block, else, free space
- Time: O(n)
- Space: Kinda big
- Use two pointers:
    - left pointer goes to next closest free space starting from left
    - right goes to next closest block space starting from right
    - once a free space is filled, move left until reaches next free space and move right until next block
    - keep doing this until the pointers have crossed:
        - this works because everything before the after the right pointer should just be a free space
        - and anything before the left pointer should have no free space
        - once your memory is in this state you are chilling
- Time: O(n)
- Space: O(1)
Things found while coding:
- input comes in one single line
"""

space = []

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

left = 0
right = len(space) - 1

while left < right:
    while left < len(space) and space[left] != ".":
        left += 1
    while right >= 0 and space[right] == ".":
        right -= 1
    
    if left > right:
        break
    else:
        space[left] = space[right]
        space[right] = "."

checksum = 0

for i, id in enumerate(space):
    if id != ".":
        checksum += i * int(id)

print("".join(space))
print(checksum)
