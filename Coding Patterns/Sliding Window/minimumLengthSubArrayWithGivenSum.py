from typing import List

'''
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''

def minSubArrayLen(s: int, nums: List[int]) -> int:

    if not nums:
        return 0
    
    l,r = 0, 0
    ans = (float("inf"), None, None)
    currentSum = 0
    while r < len(nums):
        currentSum += nums[r]

        while l <= r and currentSum >= s:
            if r - l + 1 < ans[0]:
                ans = (r-l+1, l, r)
            
            currentSum -= nums[l]
            l += 1
        r += 1
    return 0 if ans[0] == float("inf") else ans[0]

s = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(s, nums))