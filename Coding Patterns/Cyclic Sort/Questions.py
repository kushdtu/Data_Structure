
'''
Given an array containing n distinct numbers taken from 0, 1, 2, …, n, 
find the one that is missing from the array.

Example 1:
Input: [3, 0, 1]
Output: 2

Example 2:
Input: [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output: 8
'''

def missingNumber(nums):
    start = 0

    while(start < len(nums)):
        num = nums[start]
        if num < len(nums) and start != num:
            nums[start], nums[num] = nums[num], nums[start]
        else:
            start += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)

nums = [9, 6, 7, 2, 3, 5, 8, 0, 1]
# print(missingNumber(nums))

def findCombinations(input):
    # set default value is 1
    answer = 1
    prev_answer = 1
    # the prev value is 1, 2 or not
    one, two = False, False
    for i in input:
        if i == '*':
            new = answer*9
            if one:
                new += 9*prev_answer
            if two:
                new += 6*prev_answer
            one, two = True, True
        else:
            # drop it if meet 0
            new = answer if (i > '0') else 0
            if one:
                new += prev_answer
            if (two and i <= '6'):
                new += prev_answer
            one = (i == '1')
            two = (i == '2')
        prev_answer = answer
        print('prev_answer: ', prev_answer)
        answer = new % (10**9 + 7)
        print('answer: ', answer)
        print('new: ', new)
    return answer

print(findCombinations('12*'))