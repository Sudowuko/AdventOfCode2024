"""
# Goal: To multiply numbers in a corrupt files and add them together
# mul(x,y) = x * y
# all other formats of mul are invalid
# Invalid examples
# mul(4 *)
# ?(12,34)
# mul ( 2 , 4 )


# You also don't know the number of digits when multiplying
# Ex. mul(1234,43) is valid
"""


#Left number if valid will always end with a comma
def IsValidLeft(index, memory):
    print("test")
    count = 0
    length = len(memory)
    digits = ""
    x = 0
    valid = False
    print("length: ", length)
    #Check for 0th case
    if (memory[index + x].isdigit()) == False:
        print("left item break: ", {"count": 0, "digits": 0, "valid": valid}, memory[index + x])

        return {"count": 0, "digits": 0, "valid": False}
    while (x + index < length):
        print("left curr value: ", memory[index + x])
        if memory[index + x] == ",":
            valid = True
            break
        elif (memory[index + x].isdigit()): #(isinstance(memory[index + x]), int):
            count += 1
            digits += ((memory[index + x]))
            print(digits)
        else:
            valid = False
            break
        x += 1
    if (valid):
        print("left item valid: ", {"count": count, "digits": int(digits), "valid": valid})
     #   print("left item: ", {count: count, digits: int(digits), valid: True})
        return {"count": count, "digits": int(digits), "valid": valid}
    return {"count": count, "digits": int(digits), "valid": False}

    
#Right number if valid will awlays end with a )
def IsValidRight(index, memory):
    print("right index: ", index)
    count = 0
    length = len(memory)
    digits = ""
    x = 0
    valid = False
    #Check for 0th case
    if (memory[index + x].isdigit()) == False:
     #   print("left item: ", {count: 0, digits: 0, valid: False})
        return {"count": 0, "digits": 0, "valid": valid}
    while (x + index < length):
        if memory[index + x] == ")":
            valid = True
            break
        elif (memory[index + x].isdigit()): #(isinstance(memory[index + x]), int):
            count += 1
            digits += ((memory[index + x]))
        else:
            valid = False
            break
        x += 1
    if (valid):
 #       print("left item: ", {count: count, digits: int(digits), valid: True})
        return {"count": count, "digits": int(digits), "valid": valid}
    return {"count": count, "digits": int(digits), "valid": False}


def MultiplyCorruptFiles():
    f = open("3_input.txt", "r")
    input  = f.read()
    memory = list(input)
    length = len(memory)
    multi_value = 0
    sum = 0
    skip_count = 0

    for index, value in enumerate(memory):
        if (skip_count > 0):
            skip_count -= 1
            continue

        #Find initial multiply condition
        if (value == "m" and index + 2 < length):
            if memory[index + 1] == "u" and memory[index + 2] == "l":
                print("mul")
            #Check for bracket
            if memory[index + 3] == "(":
                print("index: ", index + 4)
                print("value: ", value)
                print("memory: ", memory)
                left_item = IsValidLeft(index + 4, memory)
                print("left item: ", left_item)
                #If left item is valid, get right number
                if (left_item and left_item["valid"]):
                    print("left item runs: ", left_item)
                    left_count = left_item["count"]
                    print("index: ", index)
                    right_item = IsValidRight(index + left_count + 5, memory)
                    if (right_item["valid"]):
                        print("left: ",  left_item["digits"])
                        print("right: ", right_item["digits"])
                        right_count = right_item["count"]
                        multi_value = left_item["digits"] * right_item["digits"]
                        print("multi_value: ", multi_value)
                        skip_count = left_count + right_count
        sum += multi_value
        multi_value = 0

    print("sum check:  ", sum)


                


                #Once you find the left bracket, keep track of the indexes until you find the right bracket


            
        

    

MultiplyCorruptFiles()