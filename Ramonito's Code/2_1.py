"""
Part 1:
    Input:
    - reports
        - one report per line
            - each report is list of numbers called levels
    Output:
    - return number of safe reports
        - report is safe if:
            - all levels are increasing or decreasing
                AND
            - any two adjacent levels differ by at least 1 and 3 at most
    Notes:
    - cannot rearrange levels (order of levels must stay the same)
    - considering this, seems like linear algo is most efficient
    Approach:
    - create result accumulator
    - Iterate through each line in input
        - Make this a function:
            - convert spaced out levels into array
            - keep track of prev number, prev status (inc, dec)
            - iterate through each level
                - compare current number with prev number
                    - if difference is +ve:
                        - validate status
                    - if difference is -ve:
                        - validate state
                    - validate difference
                    - update prev number (no need to update status)
                - if any validations are wrong just return 0
            - if iteration is fine without any problems, return 1
        - add return value to accumulator value
    - Time: O(n), Space: O(1)
Part 2:
- You are allowed to have one bad level
- What are the bad levels?
    - 
"""

numSafe = 0 

def checkIfSafe(levels):
    prevLevel = None
    prevStatus = None

    for level in levels:
        level = int(level)
        if not prevLevel:
            prevLevel = level
        else:
            diff = abs(level - prevLevel)
            currStatus = level > prevLevel
            if diff < 1 or diff > 3:
                return 0
            elif prevStatus is not None and prevStatus != currStatus:
                return 0
            elif prevStatus is None:
                prevStatus = currStatus
            prevLevel = level

    return 1

        

with open('2_input.txt', 'r') as file:
    for line in file:
        numSafe += checkIfSafe(line.split())

print(numSafe)