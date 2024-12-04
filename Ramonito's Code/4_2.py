"""
Update:
- Same input
Output:
- no longer of looking for XMAS in all directions
- Looking for two MAS in the form of an X
    - MAS within the X formation can be read in any direction, but A is always at center
Update to Algorithm:
- Instead of doing something at an "X", do something at an "A"
- Update Directions
    - Now want to check opposing diagonals at the same time
    - [[[-1, -1], [1, 1]], [[-1, 1], [1, -1]]]
- For each pair of directions:
    - Create a set {"M", "S"}
    - Along the first diagonal, check if value is in Set
        - if it is in set, remove it
        - if not in set, return False
    - Along next diagonal, check if value is in Set
        - if it is in set, return True
        - if not in set, return False
    - Doing it this way is a simple way of checking for the M and S XOR case rather than having multple conditions
        - also avoids check 4 elements at a time, since if the first element is wrong, itll just continue
- if both pairs return True values update result
"""

from collections import deque

wordSearch = []
diagonals = [[[-1, -1], [1, 1]], [[-1, 1], [1, -1]]]
result = 0

#Convert text to matrix
with open('4_input.txt', 'r') as file:
    for line in file:
        wordSearch.append(list(line))

numRows = len(wordSearch)
numCols = len(wordSearch[0]) - 1

def checkDiagonal(diagonal, r, c):
    validCharSet = set(["M", "S"])
    for dR, dC in diagonal:
        newR = r + dR
        newC = c + dC
        if newR in range(0, numRows) and newC in range (0, numCols) and wordSearch[newR][newC] in validCharSet:
            validCharSet.remove(wordSearch[newR][newC])
        else:
            return False
    return True

for r in range(numRows):
    for c in range(numCols):
        if wordSearch[r][c] == "A":
            result += checkDiagonal(diagonals[0], r, c) and checkDiagonal(diagonals[1], r, c)

print(result)

