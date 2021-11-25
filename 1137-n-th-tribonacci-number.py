"""
Problem Link: https://leetcode.com/problems/n-th-tribonacci-number/

The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
 
Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1
        
        first, second, third = 0, 1, 1
        for _ in range(3, n+1):
            first, second, third = second, third, first + second + third
        
        return third


class Solution1:
    def tribonacci(self, n: int) -> int:
        return self.helper(n, {0:0, 1:1, 2:1})
    
    def helper(self, n, memo):
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo) + self.helper(n-3, memo)
        return memo[n]


# TLE
class Solution2:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
