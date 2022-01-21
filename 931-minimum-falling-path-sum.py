"""
Problem Link: https://leetcode.com/problems/minimum-falling-path-sum/

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element in the next row that 
is either directly below or diagonally left/right. Specifically, the next element from position 
(row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return min(matrix[0])
        
        dp = matrix[0].copy()
        min_path = float('inf')
        
        for row in range(1, len(matrix)):
            temp = []
            for col in range(len(matrix[0])):
                min_val = dp[col] + matrix[row][col]
                if col - 1 >= 0:
                    min_val = min(min_val, matrix[row][col] + dp[col-1])
                if col + 1 < len(matrix[0]):
                    min_val = min(min_val, matrix[row][col] + dp[col+1])
                
                temp.append(min_val)
                
                if row == len(matrix) - 1:
                    min_path = min(min_path, temp[col])
            
            dp = temp
        
        return min_path
