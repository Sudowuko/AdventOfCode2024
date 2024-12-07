"""
Input:
- List of equations:
    - X : Y1 Y2 Y3 ... YK
    - X is the target number
    - Y are the numbers you can work with
    - They are all +ve integers

Output:
- Given the Ys, check if they can equal their X value when:
    - + or x operators are put between each number to some and mutiply to become the X
    - Each pair of Ys should have an operator between them

Notes:
- If all +ve numbers, x and + operators will only increase as you go from left to right
- No BEDMAS. All equations are evaluated left-to-right
- I don't think you can get a 0

Approach:
- Naive:
    - Test every single possible combination of + and x and see if any combinations work
    - Time: literally like exponential or something
- Maybe Better: Backtracking
    - Take a backtracking approach that stops once the current candidate solution is invalid
    - Start with the first number as your state
        - Candidates will be either adding or multiplying the next number
        - If at any point, the current state of the backtracking alg exceeds the value of X, we know
        that any future state built on top of this current state, will not be valid
        - So backtrack
        - The base case or solution case will be when all of the numbers are included in the state
        and the state is equal to X
            - You cant just check for when state is equal to X because you need to account for 
            an operation on all numbers.
    - Will def limit the amount of useless calculations

Example: 
"195: 10 19 5"

nums = [10, 19, 5]
state = [(None, 10), (*, 19), (+, 5)]
candidates = ["add", "multiply"]

Algorithm:
- define opeartions = ["add", "mul"]
- For every line:
    - get your nums
    - get your X
    - define flag for current line
    - define current state
        - array of tuples:
            - (operation, index of num)
    - define search function:
        - if flag is True: return -> there is no need to search if you have found a working solution
        - if current state is valid
            - for every operation
                - push (operation, latest state index + 1)
                - run search
                - pop
    - define validation;
        - write code to apply operations to numbers and get val
        - if len(state) == len(numbers) -> you have made it to the last number
            - if val is X, set flag to True
        - else: -> not all numbers in state have been considered yet
            - if val < X (assuming there are no 0s):
                - search again with current state
While testing:
- apparently only searching if val < x was missing answers
    - why??
"""

from copy import deepcopy

#Define our variables
operations = ["+", "x"]
result = 0

with open('7_input.txt', 'r') as file:
    for eq in file:
        x, rhs = eq.split(":")
        x = int(x)
        nums = rhs.split()
        totalNums = len(nums)
        initialState = [(None, 0)]
        solutions = []
        def search(state):
            # if solutions: return
            #Validate state
            val = 0
            for operation, index in state:
                num = int(nums[index])
                if operation == "x":
                    val *= num
                else:
                    val += num
            
            if len(state) == totalNums and val == x:
                # print(state, nums)
                solutions.append(deepcopy(state))
            elif len(state) < totalNums: #and val < x:
                for operation in operations:
                    state.append((operation, len(state)))
                    search(state)
                    state.pop()
        
        search(initialState)

        if solutions:
            # print(solutions)
            result += x

print(result)
                    

