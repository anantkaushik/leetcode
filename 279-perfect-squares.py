"""
Problem Link: https://leetcode.com/problems/perfect-squares/

Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 
Constraints:
1 <= n <= 104
"""
class Solution:
    
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        
        dp = [float('inf')] * (n + 1)
        
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3
        
        for i in range(4, n+1):
            j = 1
            while j * j <= i: 
                dp[i] = min(dp[i], dp[i - (j*j)] + 1)
                j += 1
        
        return dp[-1]

        
class Solution1:
    
    num_map = {}
    
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        
        if n in self.num_map:
            return self.num_map[n]
        
        min_count = n
        
        i = 1
        while i * i <= n:
            min_count = min(min_count, self.numSquares(n - i*i) + 1)
            i += 1
            
        self.num_map[n] = min_count
        return min_count
            

# TLE
class Solution2:
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        
        min_count = n
        
        i = 1
        while i * i <= n:
            min_count = min(min_count, self.numSquares(n - i*i) + 1)
            i += 1
            
        return min_count
