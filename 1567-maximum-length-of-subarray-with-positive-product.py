"""
Problem Link: https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.
A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
Return the maximum length of a subarray with positive product.

Example 1:
Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.

Example 2:
Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

Example 3:
Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].

Example 4:
Input: nums = [-1,2]
Output: 1

Example 5:
Input: nums = [1,2,3,5,-6,4,0,10]
Output: 4
 
Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        cur_positive = cur_negative = max_len = 0
        
        for num in nums:
            if num == 0:
                cur_positive = cur_negative = 0
            elif num < 0:
                cur_positive, cur_negative = (0 if cur_negative == 0 else cur_negative + 1), cur_positive + 1
            else:
                cur_positive += 1
                cur_negative = (0 if cur_negative == 0 else cur_negative + 1)
            
            max_len = max(max_len, cur_positive)
        
        return max_len
