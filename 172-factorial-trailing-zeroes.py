"""
Problem Link: https://leetcode.com/problems/factorial-trailing-zeroes/description/
Given an integer n, return the number of trailing zeroes in n!.
"""
class Solution:
    def trailingZeroes(self, n):
        count = 0
        while n:
            n //= 5
            count += n
        return count