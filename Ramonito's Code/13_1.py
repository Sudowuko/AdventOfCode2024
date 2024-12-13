"""
Input:
- Given a list of prize configurations
    - Button A movement (X, Y)
    - Button B movement (X, Y)
    - Prize Location (X, Y)
Output:
- We know it costs 3 tokens for A and 1 token for B
- Find the least cost of tokens it will take to react the prize location
- Return the fewest tokens to win ALL prizes
Notes:
- We know that it will take at most 100 total button presses to win the price
- Some prizes cannot be one
Approach:
- Minimization problem
- We know Xa = Ya, Xb = Yb, let a = a clicks, let b = b clicks
- a * Ax + b * Bx = Px
- a * Ay + b * By = Py
- (CostA / 3) * Ax + CostB * Bx = Px
- (CostA / 3) * Ay + CostB * By = Py
- Total cost = Cost A + Cost B
- Since these are both linear lines, dont you only have one intersection? 
    - Wont this intersection just be the minimum??
- CostA = (Px - CostB*Bx)*3/Ax
- ((Px - CostB*Bx)*3/Ax)/3*Ay + CostB*By = Py
- (Px - CostB*Bx)Ay/Ax + CostB*By = Py
- -CostB*Bx + Ax*CostB*By/Ay = Py*Ax/Ay - Px
- CostB = (Py*Ax/Ay - Px)/(-Bx + Ax*By/Ay)
- CostA = 3*(Px - CostB*Bx)/Ax
- Using these two equations, we can see if the two lines intersect or not
    - What happens when they don't intersect?
        - They can intersect, but if one of the costs is negative you know its not possible
- Since they are both linear lines, they will either have 1 intersection, no intersection, or infinite??
    - What happens if its infinite intersection??
        - Get the min between 
        - idk lets just do part 1 first
Algorithm:
- define variables for numerator: (Py*Ax/Ay - Px) and denominator: (-Bx + Ax*By/Ay)
- if numerator is 0, need to do for loop to get answer
- if denominator is 0, you have no answers
- else, you can calculate answers using normal equations
    - if the two numbers are not integers, it is not possible
Corner Cases While Coding:
- Running into floating point errors
    - had to round to percision
"""

result = 0

with open('13_input.txt', 'r') as file:
    count = 0
    ax, ay, bx, by, px, py = 0, 0, 0, 0, 0, 0
    for line in file:
        if len(line.split()) == 0: continue
        rule = line[:-1].split()
        if count == 0:
            ax = int(rule[2].split("+")[1][:-1])
            ay = int(rule[3].split("+")[1])
        elif count == 1:
            bx = int(rule[2].split("+")[1][:-1])
            by = int(rule[3].split("+")[1])
        elif count == 2:
            px = int(rule[1].split("=")[1][:-1])# + 10000000000000 #remove this 
            py = int(rule[2].split("=")[1])# + 10000000000000

            numerator = py * ax / ay - px
            denominator = -bx + (ax*by/ay)

            costB = (py*ax/ay - px)/(-bx + ax*by/ay)
            costA = 3*(px - costB*bx)/ax

            if costB >= 0 and costA >= 0 and round(costB, 2).is_integer() and round(costA, 2).is_integer():
                result += costB + costA
                # print(int(costB), int(costA / 3), int(costA/3 * ax + costB * bx), int(px), int(costA/3 * ay + costB * by), int(py))
            # else:
                # print(costB, costA/3, int(costA/3 * ax + costB * bx), int(px), int(costA/3 * ay + costB * by), int(py))

                
            # print(ax, ay, bx, by, px, py)
        
        if count == 2:
            count = 0
        else:
            count += 1

print(result)
