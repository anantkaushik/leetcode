"""
Problem Link: https://leetcode.com/problems/squares-of-a-sorted-array/

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, 
also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start_point = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] >= 0:
                start_point = i
                break
        
        res = []
        left, right = start_point - 1, start_point
        
        while left >= 0 and right < len(nums):
            if abs(nums[left]) > nums[right]:
                res.append(nums[right] ** 2)
                right += 1 
            else:
                res.append(nums[left] ** 2)
                left -= 1
        
        while left >= 0:
            res.append(nums[left] ** 2)
            left -= 1
        
        while right < len(nums):
            res.append(nums[right] ** 2)
            right += 1
        
        return res
