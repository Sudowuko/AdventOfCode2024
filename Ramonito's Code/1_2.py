"""
Input:
- Same as part 1
Output:
- Similarity score
    - For each number in first list, multiply by frequency in right list
    - First list will have duplicates. Still process these numbers
Naive Approach:
- For every number in first list, count how many in right list, multiply and add to similarity score
- Time: O(n*n) = O(n^2), Space: O(n)
Improved Approach:
- For every number in second list, store in a hashmap that tracks frequency of each unique number
- For every number in first list:
    - If not in hash map add 0 to similarity score
    - If in hash map: add number * freq to similarity score
- Time: O(n), Space: O(n)
"""

from collections import defaultdict

#Initializing Variables
firstList = []
secondMap = defaultdict(int)
similarityScore = 0

#Creating list and map from file
with open('1_input.txt', 'r') as file:
    for line in file:
        firstVal, secondVal = line.split()
        firstList.append(firstVal)
        secondMap[secondVal] += 1

#Calculate similarity score
for num in firstList:
    if num in secondMap:
        similarityScore += int(num) * secondMap[num]

print(similarityScore)
