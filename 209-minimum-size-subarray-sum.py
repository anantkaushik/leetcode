"""
Problem Link: https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of n positive integers and a positive integer s, find the minimal length of a 
contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]

Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time 
complexity is O(n log n). 
"""
# Time Complexity: O(N)
# Space Complexity O(1)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        index = cur_sum = 0
        min_length = len(nums) + 1
        for i in range(len(nums)):
          cur_sum += nums[i]
          while cur_sum >= s:
            min_length = min(min_length, i-index+1)
            cur_sum -= nums[index]
            index += 1
        return min_length if min_length <= len(nums) else 0

# Time Complexity: O(NlogN)
# Space Complexity O(1)
class Solution1:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        low, high = 0, len(nums)
        while low < high:
          mid = (low + high)//2
          if self.isSumPossible(nums, s, mid):
            # If this is true it means mid+1 can be the answer
            # but there maybe be exist an optimal answer which can be less than mid
            high = mid
          else:
            low = mid + 1
        return high+1 if high < len(nums) else 0
          
    # This function will check is it possible to get sum >= s with group_size no of elements.    
    def isSumPossible(self, nums, s, group_size):
      cur_sum = 0
      for i in range(len(nums)):
        cur_sum += nums[i]
        if i >= group_size:
          if cur_sum >= s:
            return True
          cur_sum -= nums[i-group_size]
      return False