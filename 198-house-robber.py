"""
Problem Link: https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will 
automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can 
rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""
# BOTTOM UP APPROACH + 2 Variables
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prev1 = prev = 0
        
        for num in nums:
            prev1, prev = prev, max(prev1 + num, prev)
        
        return prev


# BOTTOM UP APPROACH + MEMO
class Solution3:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        memo = [-1] * len(nums)
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            memo[i] = max(memo[i-2] + nums[i], memo[i-1])
        
        return memo[-1]
        

# TOP DOWN APPROACH + MEMO
class Solution2:
    def rob(self, nums: List[int]) -> int:
        self.dp = [-1] * len(nums)
        return self.helper(nums, len(nums)-1)
        
    def helper(self, nums, index):
        if index < 0:
            return 0
        
        if self.dp[index] != -1:
            return self.dp[index]
        
        self.dp[index] = max(self.helper(nums, index-2) + nums[index], self.helper(nums, index-1))
        return self.dp[index]


# TOP DOWN APPROACH
# TLE
class Solution1:
    def rob(self, nums: List[int]) -> int:
        return self.helper(nums, len(nums)-1)
        
    def helper(self, nums, index):
        if index < 0:
            return 0
        return max(self.helper(nums, index-2) + nums[index], self.helper(nums, index-1))