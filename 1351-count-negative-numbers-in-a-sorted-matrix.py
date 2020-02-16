"""
Problem Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid. 

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Example 3:
Input: grid = [[1,-1],[-1,-1]]
Output: 3

Example 4:
Input: grid = [[-1]]
Output: 1
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
"""
# Time Complexity: O(m+n)
# Space Complexity: O(1)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, column, count = m-1, 0, 0
        while row >= 0 and column < n:
          if grid[row][column] < 0:
            count += (n-column)
            row -= 1
          else:
            column += 1
        return count
        

# Time Complexity: O(m*n)
# Space Complexity: O(1)
class Solution1:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
          for j in range(len(grid[0])):
            if grid[i][j] < 0:
              count += 1
        return count