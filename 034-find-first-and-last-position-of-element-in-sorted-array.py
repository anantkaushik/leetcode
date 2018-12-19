"""
Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftIndex = self.binarySearch(nums, target, True)
        if leftIndex == len(nums) or nums[leftIndex] != target:
            return [-1,-1]
        return [leftIndex,self.binarySearch(nums, target, False)]
        
    def binarySearch(self, nums, target, flag):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] > target or (nums[mid] == target and flag):
                high = mid - 1
            else:
                low = mid + 1
        return low if flag else high