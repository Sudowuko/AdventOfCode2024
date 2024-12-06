"""
Input:
- list of rules in form : X | Y
    - this format means that if an update contains X and Y, X must be printed before Y
    - there can be multiple Y rules for a given X value
    - does not seem like rules will duplicate
    - assume rules can't contradict each other
- list of updates
    - array of numbers indicating which updates took place
    - these updates should follow the rules outlined in the prev section of input
Output:
- out of all of the correctly updated lists, return the sum of their middle updates
- what happens if the number of updates is even?
    - upon inspections of their given input, seems like nothing is even, but worth checking
    - upon checking, X and Y will always exist
    - seems like there are no duplicates in any of the lists too, but worth checking
Example:
- 47 | 53
- 47 53 60 -> Good
- 53 47 60 -> Bad
- 53 60 57 -> Good
- 47 46 69 -> Good
- 32 45 64 -> Good
Approach:
- Naive Approach:
    - For every given list of updates
        - for every element in array
            - compare with every other element in array before it
                - look at every rule for the current element
                - If a number that should exist after exists before it, return False
        - If you can go through all of the updates in a list withour return False return True
    - Time: O(n*n*n) -> for every element, compare with every other element, for every comparison look through rules
    - Space: O(n) -> Need to store data 
- Improved Naive Approach:
    - to improve the searching through the rules step, you can store all the rules in a hash map
        - key: X Value
        - value: Set of Y values that you encountered within the rules
    - Time: O(n*n)
    - Space: O(n)
- Can we improve?:
    - Only thing we can improve now is the process of checking every element before current element
    - But I don't see a way to solve this without doing that
        - The result of a previous element being valid has nothing to do with the right element
    - Maybe there is a way to create a sort of sorted form of every possible value in the rules
        - That way we know which values must for sure come before another value, but that will cause errors
        - Okay nvm just gonna stick with my quadratic solution
Algorithm: assuming every list is positive
- Create hash map:
    - Read lines until you get an empty line
        - for every line create:
            - key: X
            - value: set([Y])
            - add Y to set if X in map
- for every line after this:
    - loop through each char
        - for every char before current char
            - check if char exists in hashmap[current char]
            - if it does, return False
    - get length of list
    - return updates[length of list / 2 floored]
- return result
During Coding:
- Confirmed that update lists length is odd
- New line character exists in break between rules and update lists
- running readlines() will traverse the entire file
"""

from collections import defaultdict

#Define variables
rules = defaultdict(set)
result = 0

#Define line function
def calcLine(updates):
    for i, update in enumerate(updates):
        for j in range(i):
            if updates[j] in rules[update]:
                return 0
    
    return updates[len(updates) // 2]

with open('5_input.txt', 'r') as file:
    breakIndex = 0
    for i, line in enumerate(file):
        if i == breakIndex:
            rule = line[:-1].split("|")
            if len(rule) == 2:
                rules[rule[0]].add(rule[1])
                breakIndex = i + 1
        else:
            updates = line[:-1].split(",")
            result += int(calcLine(updates))

print(result)


