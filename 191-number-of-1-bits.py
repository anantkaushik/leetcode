"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has.

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, 
so the function should return 3.
"""
class Solution(object):
    def hammingWeight(self,n):
        return(str(bin(n)).count('1'))