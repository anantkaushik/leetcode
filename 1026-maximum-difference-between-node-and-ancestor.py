"""
Problem Link: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B 
where V = |A.val - B.val| and A is an ancestor of B.
(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

Example 1:
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7

Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Note:
The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.helper(root)
        
        
    def helper(self, root, max_val=-1, min_val=float('inf')):
        if not root:
            return 0
            
        l = self.helper(root.left, max(max_val, root.val), min(min_val, root.val))
        r = self.helper(root.right, max(max_val, root.val), min(min_val, root.val))
        
        return max(max_val - root.val, root.val - min_val, l, r)


class Solution1:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        self.helper(root)
        return self.ans
        
        
    def helper(self, root, max_val=-1, min_val=float('inf')):
        if not root:
            return 0
        
        if max_val != -1 and max_val - root.val > self.ans:
            self.ans = max_val - root.val
        if max_val != -1 and root.val - min_val > self.ans:
            self.ans = root.val - min_val
            
        self.helper(root.left, max(max_val, root.val), min(min_val, root.val))
        self.helper(root.right, max(max_val, root.val), min(min_val, root.val))
