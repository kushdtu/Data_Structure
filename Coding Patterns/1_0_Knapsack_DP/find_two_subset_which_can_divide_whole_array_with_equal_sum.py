from typing import List
class Solution:
    def canPartitionRecursive(self, dp, nums: List[int], s: int, current_index) -> bool:
        if s == 0:
            return 1
        
        if len(nums) == 0 or current_index >= len(nums):
            return 0
        
        if dp[current_index][s] == -1:
            if nums[current_index] <= s:
                if self.canPartitionRecursive(dp, nums, s - nums[current_index], current_index + 1) == 1:
                    dp[current_index][s] = 1
                    return 1
                
            dp[current_index][s] = self.canPartitionRecursive(dp, nums, s, current_index + 1)
        
        return dp[current_index][s]

    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        
        if s%2 != 0:
            return False
        
        dp = [[-1 for x in range(int(s/2) + 1)] for y in range(len(nums))]
        
        if self.canPartitionRecursive(dp, nums, int(s/2), 0) == 1:
            return True
        else:
            return False
    
    def canPartitionTabulationMethod(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        if s%2 != 0:
            return False

        s = int(s/2)
        dp = [[False for x in range(s+1)] for i in range(n)]

        for i in range(n):
            dp[i][0] = True

        for j in range(1, s+1):
            dp[0][j] = nums[0] == j

        for i in range(n):
            for j in range(s+1):
                if dp[i-1][j]:
                    dp[i][j] = dp[i-1][j]
                elif j >= nums[i]:
                    dp[i][j] = dp[i-1][j-nums[i]]

        return dp[n-1][s]