"""
Problem Link: https://leetcode.com/problems/find-peak-element/

A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.
"""
# Time Complexity: O(logN)
# Space Complexity: O(1)
class Solution(object):
    def findPeakElement(self, nums):
        first,last = 0,len(nums) - 1
        while first < last:
            mid = (first + last)//2
            if nums[mid] > nums[mid+1]:
                last = mid
            else:
                first = mid + 1
        return first

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
      if len(nums) == 1:
        return 0
      for i in range(1, len(nums)-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
          return i
      return 0 if nums[0] > nums[1] else len(nums)-1
