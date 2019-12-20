"""
Problem Link: https://leetcode.com/problems/single-number/

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using 
extra memory?
"""
class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def singleNumber(self, nums):
        res = 0
        for no in nums:
          res ^= no
        return res