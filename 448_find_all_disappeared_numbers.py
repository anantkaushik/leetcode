"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice 
and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        return list(set(range(1,n+1))-set(nums))