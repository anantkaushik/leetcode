"""
Problem Link: https://leetcode.com/problems/intersection-of-two-arrays/

Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        for n in nums1:
          d[n] = 1
          
        for n in nums2:
		  # Check if n is in dictionary and not in the result
          if n in d and d[n]:
            res.append(n)
            d[n] -= 1 # It will set the value of n = 0 which will indicate we already added n in result
        return res