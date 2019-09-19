"""
Problem Link: https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
          if i == 0 or nums[i] > nums[i-1]:
            start = i+1
            end = len(nums)-1
            while start < end:
              Sum = nums[i] + nums[start] + nums[end]
              if Sum == 0:
                res.append([nums[i],nums[start],nums[end]])
              if Sum < 0:
                curStart = nums[start]
                while curStart == nums[start] and start < end:
                  start += 1
              else:
                curEnd = nums[end]
                while curEnd == nums[end] and start < end:
                  end -= 1
        return res