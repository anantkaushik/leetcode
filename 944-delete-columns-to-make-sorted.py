"""
Problem Link: https://leetcode.com/problems/delete-columns-to-make-sorted/

We are given an array A of N lowercase letter strings, all of the same length.
Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after 
deletions is ["bef", "vyz"], and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].
(Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)
Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in 
non-decreasing sorted order.
Return the minimum possible value of D.length.
"""
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
      count = 0
      for col in zip(*A):
        if any(col[i] > col[i+1] for i in range(len(col) - 1)):
          count += 1
      return count