"""
Problem Link: https://leetcode.com/problems/increasing-subsequences/

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, 
and the length of an increasing subsequence should be at least 2.

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
 
Constraints:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of 
increasing sequence.
"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        d = set()
        for i in range(len(nums)):
            if nums[i] not in d:
                self.helper(nums, i+1, [nums[i]])
                d.add(nums[i])
                
        return self.res
        
        
    def helper(self, nums, index, arr):

        if index >= len(nums):
            return
        temp = set()
        
        for i in range(index, len(nums)):
            if nums[i] in temp:
                continue
        
            temp.add(nums[i])
            if arr[-1] <= nums[i]:
                arr.append(nums[i])
                self.res.append([i for i in arr])
                self.helper(nums, i+1, arr)
                arr.pop()

class Solution1:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.res = []
        self.helper(nums, 0)
        return self.res
        
        
    def helper(self, nums, index, arr=[]):

        if len(arr) >= 2:
            self.res.append([no for no in arr])
            
        if index == len(nums):
                return
            
        used = set()
        
        for i in range(index, len(nums)):
            if nums[i] in used or (arr and arr[-1] > nums[i]):
                continue
        
            used.add(nums[i])
            arr.append(nums[i])
            self.helper(nums, i+1, arr)
            arr.pop()