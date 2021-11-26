"""
Problem Link: https://leetcode.com/problems/climbing-stairs/description/

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2

Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3

Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        second_last_stair, last_stair = 1, 2 
        
        for _ in range(3, n+1):
            second_last_stair, last_stair = last_stair, last_stair + second_last_stair
        
        return last_stair


class Solution1:
    def climbStairs(self, n: int) -> int:
        return self.helper(n, {})
        
    def helper(self, n, memo):
        if n <= 2:
            return n
        
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        
        return memo[n]


# TLE
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
