"""
Change rounding percision to account for bigger numbers
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
