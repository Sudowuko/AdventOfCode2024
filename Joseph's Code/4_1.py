"""
Goal: To find as many instances of xmas as possible
Vertical, horitonzal, backwards, diagonal, overlapping are all valid cases

Forwards:
Horizontal: XMAS in same line
Vertical: XMAS in same index position for multiple lines

Backwards: Refers to the word being spelled backwards, not reading it backwards
Horizontal: SAMX in same line
Vertical: SAMX in same index position for multiple lines

One letter can be used for multiple cases (Ex. Horizontal and Diagonal)

Approach: For each letter in the word search, check for all possible cases. Once done, move on to the next letter and repeat
If letter starts with X, check all directions to count number of valid words for that specific X. Return total
"""
  

def FindWords(char, char_index, line, line_index, input):
    word_count = 0
    x_length = len(line)
    y_length = len(input)
    if (char == "X"):
        #Horizontal Forwards
        if char_index + 3 < x_length and line[char_index + 1] == "M" and line[char_index + 2] == "A" and (line[char_index + 3] == "S"):
            word_count += 1
        #Horizontal Backwards
        if char_index - 2 > 0 and line[char_index - 1] == "M" and line[char_index - 2] == "A" and (line[char_index - 3] == "S"):
            word_count += 1
        #Vertical Up
        if line_index - 2 > 0 and input[line_index - 1][char_index] == "M" and (input[line_index - 2][char_index] == "A" and input[line_index - 3][char_index] == "S"):
            word_count += 1
        #Vertical Down
        if line_index + 3 < y_length and input[line_index + 1][char_index] == "M" and (input[line_index + 2][char_index] == "A" and input[line_index + 3][char_index] == "S"):
            word_count += 1
        #Diagonal Up Forwards
        if char_index + 3 < x_length and line_index - 2 > 0 and input[line_index - 1][char_index + 1] == "M" and input[line_index - 2][char_index + 2] == "A" and input[line_index - 3][char_index + 3] == "S":
            word_count += 1
        #Diagonal Up Backwards
        if char_index - 2 > 0 and line_index - 2 > 0 and input[line_index - 1][char_index - 1] == "M" and input[line_index - 2][char_index - 2] == "A" and input[line_index - 3][char_index - 3] == "S":
            word_count += 1
        #Diagonal Down Fowards
        if line_index + 3 < y_length and char_index + 3 < x_length and input[line_index + 1][char_index + 1] == "M" and input[line_index + 2][char_index + 2] == "A" and input[line_index + 3][char_index + 3] == "S":
            word_count += 1
        #Diagonal Down Backwards
        if line_index + 3 < y_length and char_index - 2 > 0 and input[line_index + 1][char_index - 1] == "M" and input[line_index + 2][char_index - 2] == "A" and input[line_index + 3][char_index - 3] == "S":
            word_count += 1
    return word_count
        

def WordSearch():
    #Get input in 2D Array Form
    with open('4_input.txt', 'r') as file:
        input = []
        row = []
        for line in file:
            for char in line:
                if (char != "\n"):
                    row.append(char)
            input.append(row)
            row = []
    word_count = 0
    for line_index, line in enumerate(input):
        for char_index, char in enumerate(line):
            word_count += FindWords(char, char_index, line, line_index, input)
    print("word count: ", word_count)

    
WordSearch()