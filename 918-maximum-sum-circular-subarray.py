"""
Problem Link: https://leetcode.com/problems/maximum-sum-circular-subarray/

Given a circular integer array nums of length n, return the maximum possible 
sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array.
Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous 
element of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once. 
Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not 
exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:
Input: nums = [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:
Input: nums = [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:
Input: nums = [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

Constraints:
n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104

Solution:
There two cases:
1. When max sub array is in the middle. 
2. When max sub array = prefix + suffix
                      = total sum - middle sub array (min sub array)
Edge case: If all items are negative.  
"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max_sum = cur_min_sum = total = 0
        max_sum = min_sum = nums[0]
        
        for num in nums:
            total += num
            
            cur_max_sum = max(cur_max_sum + num, num)
            max_sum = max(max_sum, cur_max_sum)
            
            cur_min_sum = min(cur_min_sum + num, num)
            min_sum = min(min_sum, cur_min_sum)
        
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
