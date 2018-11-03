"""
Problem Link: https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        Sum = nums[0]
        result = Sum 
        for i in range(1,len(nums)):
            Sum = (Sum + nums[i]) if(Sum+nums[i]) >= nums[i] else nums[i]
            result = Sum if Sum > result else result
        return result
