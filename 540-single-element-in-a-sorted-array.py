"""
Problem Link: https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly 
twice, except for one element which appears exactly once. Find this single element that 
appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
 
Note: Your solution should run in O(log n) time and O(1) space.
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
      lo, hi = 0, len(nums) - 1
      while lo < hi:
          mid = (lo + hi) // 2
          # odd xor 1 = odd-1
          # even xor 1 = even+1
          if nums[mid] == nums[mid ^ 1]:
              lo = mid + 1
          else:
              hi = mid
      return nums[lo]
