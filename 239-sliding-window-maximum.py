"""
Problem Link: https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k which is moving 
from the very left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
# Time Complexity: O(N)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        next_greater = [0] * len(nums)
        stack = []
        
        for index in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[index]:
                stack.pop()
            
            next_greater[index] = stack[-1] if stack else len(nums) 
            stack.append(index)
        
        res = []
        max_index = 0
        for index in range(len(nums) - k + 1):
            if max_index < index:
                # to handle case where greater element of last window was the first one which is removed from the window
                max_index = index
            while next_greater[max_index] < index + k:
                max_index = next_greater[max_index]
            
            res.append(nums[max_index])
        
        return res
