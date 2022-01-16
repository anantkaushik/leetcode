"""
Problem Link: https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [height[0]]
        
        for index in range(1, len(height)):
            max_left.append(max(max_left[-1], height[index]))
        
        max_right = [0] * len(height)
        max_right[-1] = height[-1]
        
        for index in range(len(height) - 2, -1, -1):
            max_right[index] = max(max_right[index+1], height[index])
        
        total_water = 0
        for index in range(len(height)):
            total_water += min(max_left[index], max_right[index]) - height[index]
        
        return total_water
