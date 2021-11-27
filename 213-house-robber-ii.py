"""
Problem Link: https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this 
place are arranged in a circle. That means the first house is the 
neighbor of the last one. Meanwhile, adjacent houses have a security 
system connected, and it will automatically contact the police if 
two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), 
because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
 
Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if  len(nums) == 1:
            return nums[0]
        
        sl_house = nums[0]
        l_house = max(nums[0], nums[1])
        sl_house_exculding_first = 0
        l_house_exculding_first = nums[1]
        
        for index in range(2, len(nums)):
            if index < len(nums) - 1:
                sl_house, l_house = l_house, max(l_house, nums[index] + sl_house)
            
            sl_house_exculding_first, l_house_exculding_first = l_house_exculding_first, max(l_house_exculding_first, nums[index] + sl_house_exculding_first)
        
        return max(l_house, l_house_exculding_first)

# Two Pass
class Solution1:
    def rob(self, nums: List[int]) -> int:
        if  len(nums) == 1:
            return nums[0]
        
        second_last_house = nums[0]
        last_house = max(nums[0], nums[1])
        
        for index in range(2, len(nums)-1):
            second_last_house, last_house = last_house, max(last_house, nums[index] + second_last_house)
        
        res = last_house
        # excluding first
        second_last_house = 0
        last_house = nums[1]
        
        for index in range(2, len(nums)):
            second_last_house, last_house = last_house, max(last_house, nums[index] + second_last_house)
        
        return max(res, last_house)
# Memo
class Solution2:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums, len(nums)-1, False, {}), self.helper(nums, len(nums)-2, True, {}))
    
    def helper(self, nums, index, include_first, memo):
        if index < 0 or (index == 0 and not include_first):
            return 0
        
        if index not in memo:
            memo[index] =  max(self.helper(nums, index-1, include_first, memo), nums[index] + self.helper(nums, index - 2, include_first, memo))
        
        return memo[index]


# TLE
class Solution3:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums, len(nums)-1), self.helper(nums, len(nums)-2, True))
    
    def helper(self, nums, index, include_first=False):
        if index < 0 or (index == 0 and not include_first):
            return 0
        
        return max(self.helper(nums, index-1, include_first), nums[index] + self.helper(nums, index - 2, include_first))
