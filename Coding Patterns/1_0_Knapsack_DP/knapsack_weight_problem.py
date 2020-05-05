'''
Given weights and values of n items, put these items in a knapsack of capacity W to 
get the maximum total value in the knapsack. In other words, given two integer arrays
val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items 
respectively. Also given an integer W which represents knapsack capacity, find out 
the maximum value subset of val[] such that sum of the weights of this subset is 
smaller than or equal to W. You cannot break an item, either pick the complete item, 
or don’t pick it (0-1 property).
'''
from typing import List
def knapsack(Weight: int, weights: List[int], values: List[int]) -> int:
    n = len(values)
    dp = [[0 for x in range(Weight+1)] for y in range(n+1)]
    
    for i in range(n+1):
        for w in range(Weight+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][Weight]

Weight = 5
weights = [1,2,3]
values = [60, 100, 120]
# print(knapsack(Weight, weights, values))
def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in range(m):
        B.append([0] * n)
        for j in range(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B 
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
B = performOps(A)
for i in range(len(B)):
    for j in range(len(B[i])):
        print(B[i][j], end=" ")
