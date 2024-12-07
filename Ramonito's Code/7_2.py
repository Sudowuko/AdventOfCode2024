"""
Update:
- new operator: ||
    - allows you to combine current number with next number
Change to approach:
    - do same thing, just add this operator and handle it correctly in validation step
How:
- Before adding numbers, update the nums list
    - iterator through the state
    - keep track of current num
        - if operator isn't ||, add number to new list with operator
        - if operator is ||, concatenate number to current end of list, but keep operator
- With new list, just add the numbers
Update:
- its LEFT TO RIGHT, just add concat number to val
Corner Case:
- noticed that adding val <= x worked, so there is an edge case where val == x and you havent considered all the numbers yet?
"""

from copy import deepcopy

#Define our variables
operations = ["+", "x", "||"]
result = 0

with open('7_input.txt', 'r') as file:
    for eq in file:
        print(eq)
        x, rhs = eq.split(":")
        x = int(x)
        nums = rhs.split()
        totalNums = len(nums)
        initialState = [(None, 0)]
        solutions = []
        def search(state):
            #Validate state
            val = 0
            for operation, index in state:
                num = int(nums[index])
                if operation == "x":
                    val *= num
                elif operation == "||":
                    val = int(str(val) + str(nums[index]))
                else:
                    val += num
            
            if len(state) == totalNums and val == x:
                solutions.append(deepcopy(state))
            elif len(state) < totalNums and val <= x and len(solutions) == 0:
                #Continue search
                for operation in operations:
                    state.append((operation, len(state)))
                    search(state)
                    state.pop()
        
        search(initialState)

        if solutions:
            result += x

print(result)
