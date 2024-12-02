"""
Input:
- Two lists side by side
    - Each value in list is an integer
    - Seems to be positive integers
Goal:
- Given these two lists, calculate the total distance between all paired locations
    - Lists contain duplicates
    - Lists are the same size
    - paired locations: smallest number in each list is a pair, second-smallest in each is a pair, and so on
    - distance: absolute difference between to integers in a pair
Naive Approach:
- Initialize two lists for each list in input
- Find min in both, calculate diff, add to result, remove value from each list
- Return result after both lists are empty
- Time: O(n*n*n) = O(n^3), Space: O(n)
Improved Approach:
- Initialize two lists for each list input
- Sort both lists
- iterate through them at the same time while accumulating distance
- return total distance
- Time: O(nlogn), Space: O(n)
"""

#Initializing Variables
firstList = []
secondList = []
totalDist = 0

#Creating lists from file
with open('1_input.txt', 'r') as file:
    for line in file:
        firstVal, secondVal = line.split()
        firstList.append(int(firstVal))
        secondList.append(int(secondVal))

#Sorting lists
firstList.sort()
secondList.sort()

#Accumulating distance
for i in range(len(firstList)):
    totalDist += abs(firstList[i] - secondList[i])

#Printing distance
print(totalDist)
