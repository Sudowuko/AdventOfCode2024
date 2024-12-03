import copy

def part1():
    f = open("day2input.txt", "r")
    input  = f.read().splitlines()

    output = []
    report = []
    for x in input:
        for y in x.split():
            report.append(int(y))
        output.append(report)
        report = []
    

    safe_count = 0
    is_safe = True
    #Check for increasing safe condition
    x = 0
    y = 1
    length = len(output)
    while (x < length):
        report_length = len(output[x])
        # print("input increase check: ", output[x])
        while (y < report_length):
            prev = output[x][y-1]
            curr = output[x][y]
            # print("prev: ", prev)
            # print("curr: ", curr)
            if curr <= prev or abs(curr - prev) > 3:
                # print("Inc Broken: ", [prev, curr])
                is_safe = False
            y += 1

        if (is_safe):
            # print("Inc: Is Safe Check: ", output[x])
            safe_count += 1
        else:
            # print("Inc: Not Safe Check: ", output[x])
            is_safe = True
        x += 1
        y = 1
    
    #Check for decreasing safe condition
    x = 0
    y = 1
    length = len(output)
    while (x < length):
        report_length = len(output[x])
        while (y < report_length):
            prev = output[x][y-1]
            curr = output[x][y]
            if curr >= prev or abs(curr - prev) > 3:
                is_safe = False
            y += 1
      
        if (is_safe):
            safe_count += 1
        else:
            is_safe = True
        x += 1
        y = 1
    print("part 1: ")
    print("safe count: ", safe_count)
    print("safe length: ", len(output))

part1()

def part2():
    f = open("day2input.txt", "r")
    input  = f.read().splitlines()

    output = []
    backup_output = []
    report = []
    for x in input:
        for y in x.split():
            report.append(int(y))
        output.append(report)
        backup_output.append(report)

        report = []
    output_deep_copy = copy.deepcopy(output)

    safe_count = 0
    is_safe = True

    #Check for decreasing safe condition
    x = 0
    y = 1

    dampener_used = False
    length = len(output)
    #Using main output

    #Compile list of skipped items
    x_list = []

    while (x < len(output)):
        while (y < len(output[x])):
            prev = output[x][y-1]
            curr = output[x][y]
            #Bad level condition
            if curr >= prev or abs(curr - prev) > 3:
                if (dampener_used == False):
                    dampener_used = True
                    output[x].pop(y)            
                    y = 1
                else:
                    is_safe = False          
            y += 1
        if (is_safe):
          #  print("safe dec: ", output[x])
            x_list.append(x)
            safe_count += 1
        else:
            is_safe = True
        dampener_used = False
        x += 1
        y = 1

    #Check for increasing safe condition
    x = 0
    y = 1
    dampener_used = False
    length = len(output_deep_copy)
    is_safe = True
    
    #Using deep copy output since original input has been modified
    while (x < length):
        while (y < len(output_deep_copy[x])):
            prev = output_deep_copy[x][y-1]
            curr = output_deep_copy[x][y]
            #Bad level condition
            if curr <= prev or abs(curr - prev) > 3:
                
                if (dampener_used == False):
                    dampener_used = True
                    output_deep_copy[x].pop(y)            
                    y = 1
                else:
                    is_safe = False          
            y += 1
        if (is_safe):
            x_list.append(x)
            safe_count += 1
        else:
            is_safe = True
        dampener_used = False
        x += 1
        y = 1
    

    print("part 2: ")
    my_set = set(x_list)
    #Using set to see if there are any duplicates (I.e. A report that somehow passes both increasing and decreasing)
    print("x list len: ", len(x_list))
    print("set list len: ", len(my_set))

    print("safe count: ", safe_count)
    print("safe length: ", len(output))

part2()