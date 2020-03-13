"""
Problem Link: https://leetcode.com/problems/two-sum/
Given an array of integers, 
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and 
you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
# Time Complesity: O(N)
# Sapce Complexoty: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      d = {}
      for i in range(len(nums)):
        difference = target - nums[i]
        if difference in d:
          return [d[difference], i]
        d[nums[i]] = i

# Time Complesity: O(N*N)
# Sapce Complexoty: O(1)
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
        for j in range(i+1, len(nums)):
          if nums[i] + nums[j] == target:
            return [i, j]
