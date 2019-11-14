"""
Problem Link: https://leetcode.com/problems/contains-duplicate-ii/

Given an array of integers and an integer k, find out whether there are two distinct 
indices i and j in the array such that nums[i] = nums[j] and the absolute difference 
between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      d = {}
      # for i, v in enumerate(nums):
      #   if v not in d:
      #     d[v] = i
      #   else:
      #     if i - d[v] <= k:
      #       return True
      #     else:
      #       # if we found a key, but was at a distance more than K
      #       # we set this index as a last_indiex, future comparison will be
      #       # based on this index.
      #       d[v] = i
      # return False
      for i, v in enumerate(nums):
          if v in d and i - d[v] <= k:
              return True
          d[v] = i
      return False