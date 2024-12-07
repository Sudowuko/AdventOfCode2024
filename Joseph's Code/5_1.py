"""
Goal: To get the sum of every middle correct input

Steps Required: Get two separate input lists (X) and (Y)

Create own custom order that follows all the rules

For each element on the left side, check all corresponding values that need to be before it

Ex. 47 has to be printed before both 53 and 13

To solve:

Create a dictionary of left keys with all the associated values before it
For each associated value, that becomes the new key for the new associated values

Using dictionary:

First element is 75
Go to 75 key and see if 47 is there, 47 exists and is a valid element
Go to 47 key and see if 61 is there, 61 exists and is a valid element
Go to 61 key and see if 53 is there, 53 exists and is a valid element
Go to 53 key and see if 29 is there, 29 exists and is a valid element

91 is valid
Check if 61 is in 97's dictionary, 61 is valid
Check if 53 is in 61's dictionary, 53 is valid
Check if 29 is in 53's dictionary, 29 is valid
Check if 13 is in 29's dictionary, 13 is valid

If an element is not immediately there, check each element in the array as the key for the next array

"""

def PageOrder():
    #Create left and right input arrays
    with open('5_input.txt', 'r') as file:
        page_orders = []
        page_updates = []
        single_update = []
        for index, line in enumerate(file):
            if line == "\n":
                break
            updated_page = str(line.split()).replace("['", "").replace("']", "")
            page_orders.append(updated_page.split("|"))
        
        for line in (file):
            for item in line.split(","):
                single_update.append((int(item)))
            page_updates.append(single_update)
            single_update = []
        
    left_array = []
    right_array = []
    for value in page_orders:
        left_array.append(int(value[0]))
        right_array.append(int(value[1]))

    #Create dictionary purely for left side elements as the keys
    page_dict = {}
    for index, value in enumerate(left_array):
        if value not in page_dict:
            page_dict[value] = [right_array[index]]
        else:
            page_dict[value].extend([right_array[index]])
    correct_page_updates = []
    current_page_update = []

    for index, page_update in enumerate(page_updates):
        #First item in update is always true
        current_page_update.append(page_update[0])
        for row_index, item in enumerate(page_update):
            #Skip first item since it's already been added
            if row_index == 0:
                row_index += 1
            current_key = item
            previous_key = page_update[row_index - 1]
            #If the current key is in the values associated with the previous key, it is a valid element
            if (page_dict.get(previous_key)):
                if current_key in page_dict[previous_key]:
                    current_page_update.append(item)
        #If the lengths are unequal some rules would have been broken
        if len(current_page_update) == len(page_update):
            correct_page_updates.append(page_update)
        current_page_update = []
    #Using all the correct orders get the sum of every middle element
    sum = 0
    for correct_page_update in correct_page_updates:  
        middle_index = (len(correct_page_update))//2
        sum += correct_page_update[middle_index]
    print("sum: ", sum)
    
PageOrder()

