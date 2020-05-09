from typing import List

'''
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
'''
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        maxLen = 0
        l, r = 0, 0
        count = 0
        while r < len(A):
            if A[r] != 1:
                count += 1
                
            while count > K:
                if A[l] == 0:
                    count -= 1
                l += 1
            
            maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen
