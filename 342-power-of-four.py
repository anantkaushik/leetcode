"""
Problem Link: https://leetcode.com/problems/power-of-four/description/

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:
Input: 16
Output: true

Example 2:
Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?
"""
class Solution(object):
    def isPowerOfFour(self, num):
        bin_num = bin(num)[2:]
        c = bin_num.count('0')
        return True if bin_num[0] == '1' and c == len(bin_num) - 1 and c % 2 == 0 else False