'''
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, 
LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited 
resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best 
way to maximize its total capital after finishing at most k distinct projects.

You are given several projects. For each project i, it has a pure profit Pi and a minimum capital 
of Ci is needed to start the corresponding project. Initially, you have W capital. When you finish a 
project, you will obtain its pure profit and the profit will be added to your total capital.

To sum up, pick a list of at most k distinct projects from given projects to maximize your final capital, 
and output your final maximized capital.

Example 1:

Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

Output: 4

Explanation: Since your initial capital is 0, you can only start the project indexed 0.
             After finishing it you will obtain profit 1 and your capital becomes 1.
             With capital 1, you can either start the project indexed 1 or the project indexed 2.
             Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the 
             maximum capital.
             Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
'''
from heapq import heappop, heappush
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        n = len(Profits)
        cache = []
        for i in range(n):
            cache.append((Capital[i], Profits[i]))
        cache.sort(key = lambda x:x[0]) # O(NLogN)
        
        index = 0
        maxHeap = []
        
        while k:
            for i in range(index, n):
                if cache[i][0] <= W:
                    heappush(maxHeap, -cache[i][1])
                    index = i+1
                else:
                    break
            if not maxHeap:
                break
            
            W += -heappop(maxHeap)
            k -= 1
        
        return W
        