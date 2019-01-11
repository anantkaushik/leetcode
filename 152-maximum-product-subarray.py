"""
Problem Link: https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has 
the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxp = minp = res = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                maxp, minp = minp, maxp
            maxp = max(nums[i], nums[i]*maxp)
            minp = min(nums[i], nums[i]*minp)
            res = max(res, maxp)
        return res