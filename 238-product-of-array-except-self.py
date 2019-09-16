"""
Problem Link: https://leetcode.com/problems/product-of-array-except-self/description/

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements 
of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity 
analysis.)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        res = []
        for i in range(len(nums)):
          res.append(p)
          p *=  nums[i]
        p = 1
        for i in range(len(nums)-1,-1,-1):
          res[i] = res[i] * p
          p *= nums[i]
        return res