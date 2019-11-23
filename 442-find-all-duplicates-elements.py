"""

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice 
and others appear once.
Find all the elements that appear twice in this array.

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
          index = abs(nums[i]) - 1
          if nums[index] < 0:
            res.append(index+1)
          nums[index] = -nums[index]
        return res
