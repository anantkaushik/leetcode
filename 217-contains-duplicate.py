"""

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
    
# Little better solution as if we found duplicate element we break 
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for i in nums:
          if i in temp:
            return True
          temp.add(i)
        return False
