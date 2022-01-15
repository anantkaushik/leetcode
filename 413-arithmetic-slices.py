"""
Problem Link: https://leetcode.com/problems/arithmetic-slices/

An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

Example 2:
Input: nums = [1]
Output: 0

Constraints:
1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        diff =  float('inf') 
        ap_arrays = cur_length = 0
        
        for index in range(1, len(nums)):
            if nums[index] - nums[index-1] == diff:
                cur_length += 1
            else:
                diff = nums[index] - nums[index-1]
                cur_length = 2
            
            if cur_length >= 2:
                ap_arrays += (cur_length - 2)
        
        return ap_arrays
