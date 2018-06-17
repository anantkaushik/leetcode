"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        t = [1] + [0] * n
        for i in nums:
            if i >= 1 and i <= n:
                t[i] = 1
        j = 1
        while j <= n:
            if t[j] == 0:
                return j
            j +=1
        return n+1