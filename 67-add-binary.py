"""
Problem Link: https://leetcode.com/problems/add-binary/

Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""
# there are two cases for every bit
# 1. they are equal
#       - 1 and 1  -> 0 but result will depend on carry.
#       - 0 and 0  -> 0 but result will depend on carry
#         [if carry is 1, res = 1, if carry is 0, res = 0]
#  2. they are unequal
#       - 1 and 0  -> result carry + 1  -> result = carry === 0 ? 1 : 0
#       - 0 and 1  -> result carry + 1  -> result = carry === 0 ? 1 : 0
#       don't touch the carry because if it was 0, it will remain 0 even after this sum
#       why?
#           - carry = 0, now bits are: 1 + 0 = 1. Add carry: 1 + 0(carry) -> carry will remain 0
#           - carry = 1, now bits are: 1 + 0 = 1. Add carry: 1 + 1(carry) -> carry will remain 1
class Solution:
    # Method 1
    def addBinary(self, a: str, b: str) -> str:
      res = []
      i = len(a) - 1
      j = len(b) - 1
      carry = '0'
      while i >= 0 or j >=0:
        ach = a[i] if i >= 0 else '0'
        bch = b[j] if j >= 0 else '0'
        if ach == bch:
          res.append(carry)
          carry = ach
        else:
          res.append('1' if carry == '0' else '0')
        i -= 1
        j -= 1
      
      if carry == '1':
        res.append(carry)
      
      return ''.join(res[::-1])

    # Method 2
    def addBinary_integer(self, a: str, b: str) -> str:
      res = []
      i = len(a) - 1
      j = len(b) - 1
      carry = 0
      while i >= 0 or j >=0:
        ach = int(a[i]) if i >= 0 else 0
        bch = int(b[j]) if j >= 0 else 0
        summ = ach + bch + carry
        res.append(str(summ%2))
        carry = 1 if summ > 1 else 0
        i -= 1
        j -= 1
      
      if carry == 1:
        res.append(str(carry))
      
      return ''.join(res[::-1])

    # Method 3
    def addBinary_xor(self, a: str, b: str) -> str:
      res = []
      i = len(a) - 1
      j = len(b) - 1
      carry = 0
      while i >= 0 or j >= 0 or carry > 0:
        ach = ord(a[i]) - ord('0') if i >= 0 else 0
        bch = ord(b[j]) - ord('0') if j >= 0 else 0
        res.append(str(ach ^ bch ^ carry))
        carry = (ach+bch+carry) >> 1 # It is equivalent to (a+b+c)/2
        i -= 1
        j -= 1

      return ''.join(res[::-1])