"""
Problem Link: https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's 
and return its area.

Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
class Solution:
    # Time Complexity: O(mn)
    # Space Complexity: O(m)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
          return 0
        dp = [0] * (len(matrix[0]))
        res = prev = 0
        for i in range(len(matrix)):
          for j in range(len(matrix[0])):
            temp = dp[j]
            if i == 0 or j == 0:
              dp[j] = 1 if matrix[i][j] == "1" else 0 
            elif matrix[i][j] == "1":
              dp[j] = min(dp[j-1],prev,dp[j]) + 1
            else:
              dp[j] = 0
            prev = temp
            res = max(res,dp[j])
        return res*res