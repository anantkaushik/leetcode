"""
Problem Link: https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 
(where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true

Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
# Using Floyd Cycle detection algorithm
class Solution:
    def isHappy(self, n: int) -> bool:
      slow = n
      fast = self.squareSum(self.squareSum(n))
      while fast != slow:
        slow = self.squareSum(slow)
        fast = self.squareSum(self.squareSum(fast))
      return fast == 1
        
    def squareSum(self, n):
      new_no = 0
      while n:
        new_no += (n%10) * (n%10)
        n //= 10
      return new_no

class Solution1:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 6:
            nextN = 0
            while(n):
                nextN += (n%10) * (n%10)
                n //= 10
            n = nextN
        return n == 1

class Solution2:
    def isHappy(self, n: int) -> bool:
      temp = set()
      while n:
        if n == 1:
          return True
        temp.add(n)
        new_no = self.squareSum(n)
        if new_no in temp:
          return False
        n = new_no
        
    def squareSum(self, n):
      new_no = 0
      while n:
        new_no += (n%10) * (n%10)
        n //= 10
      return new_no