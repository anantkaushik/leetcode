"""
Problem Link: https://leetcode.com/problems/split-array-largest-sum/

Given an array which consists of non-negative integers and an integer m, you can split the array into m 
non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
      # if m = n then the largest sum will be maximum number
      low = max(nums)
      
      # if m = 1 then maximum sum will be the sum of all the numbers 
      high = sum(nums)
      
      while low < high:
        mid = (low+high)//2
        # if number of cuts <= m
        # we have to decrease the mid value, so that we
        # can make more groups
        # since it can be our potential answer, we'll keep it
        # in our search space.
        if self.canSplit(nums, mid, m):
          high = mid
        else:
          # if number of cuts > m
          # we need to increase the mid value we've chosen
          # so that we can make fewer group.
          low = mid + 1

      
      return low
    
    def canSplit(self, nums, mid, m):
      subArraySum = 0
      count = 1
      for n in nums:
        subArraySum += n
        if subArraySum > mid:
          count += 1
          subArraySum = n
          if count > m: return False
      return True
