"""
Input:
- Word Search
- File of characters
- Characters are letters X, M, A, or S
Output:
- Return the total number of occurences of the word XMAS
    - An occurence can be found vertically, horizontally, and diagonally
    - Occurence can be read forward or backward
    - Occurence can overlap other occurences as well
Example:
[
    XMAS
    MMAS
    AXAA
    SSSS
]

Has three total occurences: 1 horizontal, 1 vertical, 1 diagonal
Approach:
- Naive:
    - Convert file input into matrix
    - look for all horizontal occurences, look for all vertical occurences, look for all diagonal occurences
        - This would be done by checking every possible horizontal, vertical, and diagonal substring
        - Then do the same thing for the backwards occurences
    - Time: technically O(n) since substrings being checked are always just size 4. But doing a lot of repeated or unneeded calcs
    - Space: O(n) since need to make a matrix to store input
- Possible Improvement:
    - At every "X" character only, check all 8 possible directions.
        - if any direction finds the correct next letter, continue traversing in that direction, 
        - once the string XMAS is found, stop traversing and increment counter
    - This will avoid checking all 8 * 4 possible characters, and instead only read characters that support a valid solution
    - Worst Case: XMAS can be found in every direction:
        - 
        [     
            S  S  S
             A A A
              MMM 
            SAMXMAS
              MMM
             A A A
            S  S  S
        ]
    - Since all words can overlap, any MAS characters can be used in another XMAS solution, so need to check at every X
    - Time: More O(n), Space: O(n)
    - Since direction is being used, can make solution more modifiable if say change in direction is allowed in part 2

Algorithm:
- Convert file input into matrix
- Create valid directions array
- Iterate through the matrix
- If do not encounter X, do nothing
- If X, start a for loop
    - This will go into each possible direction:
        - declare a queue with form [X, M, A, S]
            - Queue is good hear since we want to just check order and i dont wanna use Indices 
        - While we have values in the queue:
            - pop from queue, compare the current index
            - if equal, update index in same direction and continue
            - id not equal, break
        - if there are values in the queue, do nothing
        - if the queue is empty, increment result by 1
- return result

Corner Cases:
- Noticed '\n' in characters, so need to account for that in numCols
"""

from collections import deque

wordSearch = []
directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, 1], [1, -1]]
result = 0

#Convert text to matrix
with open('4_input.txt', 'r') as file:
    for line in file:
        wordSearch.append(list(line))

numRows = len(wordSearch)
numCols = len(wordSearch[0]) - 1

def checkAlongDirection(dR, dC, r, c):
    validCharQueue = deque(["X", "M", "A", "S"])
    newR = r
    newC = c
    while validCharQueue:
        validChar = validCharQueue.popleft()
        if newR in range(0, numRows) and newC in range (0, numCols) and wordSearch[newR][newC] == validChar:
            newR += dR
            newC += dC
        else:
            return 0
    if len(validCharQueue) == 0:
        return 1

for r in range(numRows):
    for c in range(numCols):
        if wordSearch[r][c] == "X":
            for dR, dC in directions:
                result += checkAlongDirection(dR, dC, r, c)

print(result)

