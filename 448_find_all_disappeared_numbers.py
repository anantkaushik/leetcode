"""
Problem Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice 
and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
      for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
          nums[index] *= -1
      return [i+1 for i in range(len(nums)) if nums[i] > 0]
        
