
'''
3Sum
Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

def findThreeSum(nums):
    nums.sort()
    n = len(nums)
    result = set()
    for i in range(n-2):
        l = i+1
        r = n-1
        while(l < r):
            if nums[i] + nums[l] + nums[r] == 0:
                result.add((nums[i], nums[l], nums[r]))

            if nums[i] + nums[l] + nums[r] < 0:
                l += 1
            else:
                r -= 1
    newResult = []
    for j in result:
        newResult.append(list(j))
    return newResult

nums = [-1, 0, 1, 2, -1, -4]
# print(findThreeSum(nums))

'''
Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that each 
element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums 
being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums
being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.
'''

def removeDuplicate(nums):
    n = len(nums)
    if n == 0 or n == 1:
        return n

    j = 0
    for i in range(n-1):
        if nums[i] != nums[i+1]:
            nums[j] = nums[i]
            j += 1

    nums[j] = nums[n-1]
    return j+1

nums = [0,0,1,1,1,2,2,3,3,4]
# print(removeDuplicate(nums))

'''
Trapping Rain Water
Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

def trapWater(height):
    n = len(height)
    lo = 0
    hi = n - 1
    left_max = 0
    right_max = 0
    result = 0

    while (lo <= hi):
        if (height[lo] < height[hi]):
            if (height[lo] > left_max):
                left_max = height[lo]
            else:
                result += left_max - height[lo]
            lo += 1
        else:
            if (height[hi] > right_max):
                right_max = height[hi]
            else:
                result += right_max - height[hi]
            hi -= 1
    return result

height = [0,1,0,3,0,2,0,4,0,2,0,4]
print(trapWater(height))