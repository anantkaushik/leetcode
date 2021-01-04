"""
Problem Link: https://leetcode.com/problems/beautiful-arrangement/

Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a 
beautiful arrangement if for every i (1 <= i <= n), either of the following is true:
perm[i] is divisible by i.
i is divisible by perm[i].

Given an integer n, return the number of the beautiful arrangements that you can construct.

Example 1:
Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 15
"""
class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n+1))
        self.count = 0
        self.permute(nums, 0)
        return self.count
    
    def permute(self, nums, pos):
        if pos == len(nums):
            self.count += 1
        
        for i in range(pos, len(nums)):
            nums[i], nums[pos] = nums[pos], nums[i]
            if (nums[pos] % (pos + 1) == 0) or ((pos + 1) % nums[pos] == 0):
                self.permute(nums, pos+1)
            nums[i], nums[pos] = nums[pos], nums[i]


# Time Complexity -> O(n!)
# TLE
class Solution1:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n+1))
        self.count = 0
        self.permute(nums, 0)
        return self.count
    
    def permute(self, nums, pos):
        if pos == len(nums) - 1 and self.isValid(nums):
            self.count += 1
        
        for i in range(pos, len(nums)):
            nums[i], nums[pos] = nums[pos], nums[i]
            self.permute(nums, pos+1)
            nums[i], nums[pos] = nums[pos], nums[i]
            
        
    
    def isValid(self, nums):
        
        for k in range(1, len(nums)+1):
            if nums[k-1] % k != 0 and k % nums[k-1] != 0:
                return False
        
        return True
