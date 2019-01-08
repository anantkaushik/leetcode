"""
Problem Link: https://leetcode.com/problems/pascals-triangle/

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        res = []
        for i in range(numRows):
            row = [1]*(i+1)
            res.append(row)
            for j in range(1,len(row)-1):
                res[i][j] = res[i-1][j-1]+res[i-1][j] 
        return res