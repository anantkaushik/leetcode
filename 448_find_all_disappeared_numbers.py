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
        temp = [0]*len(nums)
        for i in range(len(nums)):
            temp[nums[i]-1] = 1
        return [i+1 for i in range(0,len(nums)) if not temp[i]]
