"""
Part 2:
- You are allowed to remove one bad level
- What are the bad levels you can encounter?
    - status changes, diff okay?
        - 1 3 1 4: You would remove 1
        - 2 5 3 4: You would remove 5
        - 2 5 1 4: Invalid
    - status changes, diff too big?
        - 1 3 0 4: You would remove 0
        - 10 13 9 8: You would remove 13
        - 10 13 9 11: Invalid
    - status stays the same, but too big diff
        - 1 3 10 4: You would remove 10
        - 1 3 10 10: Invalid
- I think im going too crazy
Approach:
- Remove means no longer consider
- Once we encounter a bad level, keep track of
current index and prev index it
    - This is because you can either remove
    one or the other to validate the levels
- With these indices, run another iteration
through levels ignoring currIndex.
    - if there is still a problem
        - iterate again, ignoring the prevIndex instead
            - if there is still a problem, return 0
    - return 1
- DOES NOT WORK
- badLevelIndex = 3, counter = 2, poppedIndex = badLevelIndex - counter
- Example: [7, 8, 10, 9, 7, 6, 5] -> would remove 8 even if bad level is 7 or 9
- How do we know which level to remove???
- Whatever, lets just test every possible letter
Final Approach -> Probably Naive because i cant think of anything else for now:
- Iterate normally, if bad level found
    - try removing elements one by one and reiterating, starting from bad element
    and going backwards. (might even just be 3 elements to care about)
- [5, 6, 7, 9, 8]
"""

numSafe = 0 

def isBadLevel(diff, currStatus, prevStatus):
    return (diff < 1 or diff > 3) or (prevStatus is not None and prevStatus != currStatus)


def checkIfSafe(levels):
    prevLevel = None
    prevStatus = None
    badLevelFound = False
    badLevelIndex = -1


    for i, level in enumerate(levels):
        level = int(level)
        if not prevLevel:
            prevLevel = level
        else:
            diff = abs(level - prevLevel)
            currStatus = level > prevLevel
            if isBadLevel(diff, currStatus, prevStatus):
                badLevelFound = True
                badLevelIndex = i
                break
            elif prevStatus is None:
                prevStatus = currStatus
            prevLevel = level

    if badLevelFound:
        counter = 2
        while(counter >= 0):
            badLevelFound = False
            ignoreIndex = badLevelIndex - counter
            if ignoreIndex >= 0:
                # ignoredLevel = levels.pop(ignoreIndex)
                prevLevel = None
                prevStatus = None
                for i, level in enumerate(levels):
                    if i == ignoreIndex:
                        continue
                    level = int(level)
                    if not prevLevel:
                        prevLevel = level
                    else:
                        diff = abs(level - prevLevel)
                        currStatus = level > prevLevel
                        if isBadLevel(diff, currStatus, prevStatus):
                            badLevelFound = True
                            break
                        elif prevStatus is None:
                            prevStatus = currStatus
                        prevLevel = level
                if not badLevelFound:
                    return 1
                # levels.insert(ignoreIndex, ignoredLevel)
            counter -= 1
        return 0
    else:
        return 1
        

with open('2_input.txt', 'r') as file:
    for line in file:
        numSafe += checkIfSafe(line.split())

print(numSafe)