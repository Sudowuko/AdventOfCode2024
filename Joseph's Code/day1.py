def part1():
    f = open("day1input.txt", "r")
    input  = f.read()
    left_array = []
    right_array = []
    switch = True

    for x in input.split():
        if (switch):
            left_array.append(int(x))
            switch = False
        else:
            right_array.append(int(x))
            switch = True

    final_left_array = sorted(left_array)
    final_right_array = sorted(right_array)
    x = 0
    xlen = len(left_array)
    diff = 0
    while (x < xlen):
        diff += abs(final_left_array[x] - final_right_array[x])
        x += 1
    print("diff: ", diff)

part1()

def part2():
    f = open("day1input.txt", "r")
    input  = f.read()
    left_array = []
    right_array = []
    switch = True

    for x in input.split():
        if (switch):
            left_array.append(int(x))
            switch = False
        else:
            right_array.append(int(x))
            switch = True

    x = 0
    xlen = len(left_array)
    score = 0
    for x in left_array:
        count = right_array.count(x)
        score += count * x
        
    print("score: ", score)

part2()

