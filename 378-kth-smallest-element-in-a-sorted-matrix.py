"""
Problem Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given a n x n matrix where each of the rows and columns are sorted in ascending order, 
find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.

Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
from Queue import PriorityQueue
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        p = PriorityQueue()
        row = len(matrix)
        for c in range(row):
            p.put((matrix[0][c],0,c))
        for i in range(k-1):
            val,r,c = p.get()
            if r == row - 1:
                continue
            p.put((matrix[r+1][c],r+1,c))
        val,r,c = p.get()
        return val