"""

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice 
and others appear once.
Find all the elements that appear twice in this array.

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
class Solution(object):
    def findDuplicates(self, nums):
        result = []
        dup = {}
        for i in nums:
            if i in dup:
                result.append(i)
            else:
                dup[i] = 1
        return result