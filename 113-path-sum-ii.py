"""
Problem Link: https://leetcode.com/problems/path-sum-ii/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.ans = []
        self.dfs(root, sum)
        return self.ans
        
    def dfs(self, root, sum, arr=[], cur_sum=0):
        if not root:
            return cur_sum
        
        cur_sum += root.val
        arr.append(root.val)
        
        if not root.left and not root.right and cur_sum == sum:
            self.ans.append([num for num in arr])
        
        self.dfs(root.left, sum, arr, cur_sum)
        self.dfs(root.right, sum, arr, cur_sum)
        
        arr.pop()
