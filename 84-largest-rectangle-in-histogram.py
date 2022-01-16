"""
Problem Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

Given an array of integers heights representing the histogram's bar height where the width of each 
bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
 
Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
"""
# Time Complexity: O(N)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lb = []  # left boundary
        stack = []
        
        for index in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[index]:
                stack.pop()
            
            lb.append(stack[-1] if stack else -1)
            stack.append(index)
        
        rb = [0] * len(heights) # right boundary
        stack = []
        
        for index in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[index]:
                stack.pop()
            
            rb[index] = stack[-1] if stack else len(heights)
            stack.append(index)
        
        max_area = 0
        for index in range(len(heights)):
            width = rb[index] - lb[index] - 1
            max_area = max(max_area, width * heights[index])
        
        return max_area
