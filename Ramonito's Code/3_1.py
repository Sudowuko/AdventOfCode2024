"""
Input:
- Text of characters
- Within this text, there are random substrings and substrings that follow
the mul(x,y) format
Output:
- Within this text, only perform the multiplication operations of the valid
mul(x,y) calls
- Return the sum of all multiplication calls
- x and y are both supposed to be 1-3 digit numbers
- A valid mul call has to be in the format of: mul(x,y), where x and y are 1-3 
digit numbers
Examples:
- mul(3,5) -> good
- adasdadasdmmul(3,5)asdasdasd -> good
- mul(3333,5) -> bad (too many digits)
- ml(3,5), mul (3,5), mul(3, 5) -> bad because not right format
- Therefore need to have right format, and only 1 to three digits
Approach:
- Need to look for format and for number of digits
    - Correct Format: mul([1-3 digit number],[1-3 digit number])

- Naive Approach:
    - have checks that go across the entire text checking each possible valid substring
    - mul(*, *), mul(*,**), mul(*,***), ... and so on
    - Time: O(n) -> There are a finite number of valid substring formats, 
    but this is still pretty inefficient and hard to implement

- Possible strictly linear approach (Sliding Window?):
    - have a list of characters you should encounter in order
        - validChars: ["m", "u", "l", "(", ",", ")"]
    - have a validPointer that starts at index 0 of validChars
    - As right of sliding window parses line
        - if char at right matches pointer in validChars, do not move left
            - increment pointer in validChars and continue moving right
        - If one of the valid chars is not met, reset left equal to right,
        rest validPointer, and continue
        - if all valid chars are met, validChars pointer should leave validChars
        array, this indicates that a valid command was found
            - compute product, add to result, reset validPointer, reset left = right
    - Special Valid Chars:
        - When validPointer is on ","
            - Start recording and looking for first number
                - If any char is not a number, reset everything
                - If there ends up being more than 3 numbers, reset everything
                - If you run into a "," before these conditions are met
                    - Save the current number and move on
        - When valid Pointer is on ")"
            - Start recording and looking for second number
                - follow same steps but for ")" instead of ","
    - Time: O(n) -> Only one single pass of entire input
    - Space: O(1) -> validChars is of fixed size
    - Improvement: Do not need left pointer (validPointer is sufficient)
        - Could also use a stack, but fixed validChars (no need)
    - Edge Case found: "mulmul(2,3)"
        - Mu code will switch to look for "m" at the second "m" but not actually
        consider that "m"
        - Maybe just check if character is an "m" and if it is, move valid pointer

"""

#Declare Variables
validChars = ["m", "u", "l", "(", ",", ")"]
validPointer = 0
res = 0
firstNum = ""
secondNum = ""


#Creating lists from file
with open('3_input.txt', 'r') as file:
    for line in file:
        for char in line:
            currValidChar = validChars[validPointer]
            if currValidChar == ",":
                numDigits = len(firstNum)
                if char == "," and numDigits > 0:
                    validPointer += 1
                elif char.isdigit() and numDigits < 3:
                    firstNum += char
                else:
                    if char == "m":
                        validPointer = 1
                    else:
                        validPointer = 0
                    firstNum = ""
            elif currValidChar == ")":
                numDigits = len(secondNum)
                if char == ")" and numDigits > 0:
                    validPointer = 0
                    res += int(firstNum) * int(secondNum)
                    firstNum = ""
                    secondNum = ""
                elif char.isdigit() and numDigits < 3:
                    secondNum += char
                else:
                    if char == "m":
                        validPointer = 1
                    else:
                        validPointer = 0
                    firstNum = ""
                    secondNum = ""
            elif char == currValidChar:
                validPointer += 1
            else:
                if char == "m":
                    validPointer = 1
                else:
                    validPointer = 0

#Print Result
print(res)
        
