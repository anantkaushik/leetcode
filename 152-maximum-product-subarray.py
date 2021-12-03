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
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = res = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod
                
            max_prod = max(nums[i], nums[i] * max_prod)
            min_prod = min(nums[i], nums[i] * min_prod)
            res = max(res, max_prod)
            
        return res

# TLE
class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        
        for i in range(len(nums)):
            cur_prod = 1
            for j in range(i, len(nums)):
                cur_prod *= nums[j]
                max_prod = max(max_prod, cur_prod)
        
        return max_prod
