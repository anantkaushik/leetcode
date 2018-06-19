"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
"""
class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        return num % 9 if num % 9 !=0 else 9 #reference- https://en.wikipedia.org/wiki/Digital_root
