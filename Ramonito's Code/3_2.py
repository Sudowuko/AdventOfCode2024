"""
Input:
- Same input as before
- There are now three possible commands to look out for:
    - do()
    - don't()
    - mul([1-3 digit number],[1-3 digit number])
Output:
- Return sum of all products
- When you encounter a don't(), this disables all ops until you encounter
a do()
- When you encounter a do(), this will enable all ops until you encounter
a don't()
- Starts in enabled mode
- mul() commands stays the same
Approach:
- Now we need to look for 3 possible commands
- depending on which command is found, perform 3 separate actions
- Can think of it as moving 3 separate valid pointers
    - The first valid pointer that reaches the end of its validCharsMul performs the given command
    - you can never have two validCharsMul perfrom at the same time
- Add two more validChar arrays
- Add two more validChar pointers
- On top of the existing conditions, add 2 more decision statements (you want to update all valid
pointers on each character)
- Corner Case: if disabled, my code was not going to check for an "m"
    - Solution: Keep on tracking mul characters even in disabled, so that you can still 
    check if the current char is an "m". Move is enabled to simply updating result
"""

#Declare Variables
validCharsMul = ["m", "u", "l", "(", ",", ")"]
validCharsDo = ["d", "o", "(", ")"]
validCharsDont = ["d", "o", "n", "'", "t", "(", ")"]
pMul = 0
pDo = 0
pDont = 0
firstNum = ""
secondNum = ""
isEnabled = True
res = 0


#Creating lists from file
with open('3_input.txt', 'r') as file:
    for line in file:
        for char in line:

            #Handles checking for valid mul() command
            validMul = validCharsMul[pMul]
            if validMul == ",":
                numDigits = len(firstNum)
                if char == "," and numDigits > 0:
                    pMul += 1
                elif char.isdigit() and numDigits < 3:
                    firstNum += char
                else:
                    if char == "m":
                        pMul = 1
                    else:
                        pMul = 0
                    firstNum = ""
            elif validMul == ")":
                numDigits = len(secondNum)
                if char == ")" and numDigits > 0:
                    pMul = 0
                    if isEnabled:
                        res += int(firstNum) * int(secondNum)
                    firstNum = ""
                    secondNum = ""
                elif char.isdigit() and numDigits < 3:
                    secondNum += char
                else:
                    if char == "m":
                        pMul = 1
                    else:
                        pMul = 0
                    firstNum = ""
                    secondNum = ""
            elif char == validMul:
                pMul += 1
            else:
                if char == "m":
                    pMul = 1
                else:
                    pMul = 0

            #Handles checking for valid do() command    
            validDo = validCharsDo[pDo]
            if validDo == ")" and char == validDo:
                isEnabled = True
                pDo = 0
            elif char == validDo:
                pDo += 1
            else:
                if char == "d":
                    pDo = 1
                else:
                    pDo = 0

            #Handles checking for valid don't() commands
            validDont = validCharsDont[pDont]
            if validDont == ")" and char == validDont:
                isEnabled = False
                pDont = 0
            elif char == validDont:
                pDont += 1
            else:
                if char == "d":
                    pDont = 1
                else:
                    pDont = 0

#Print Result
print(res)
        
