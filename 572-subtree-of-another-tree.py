"""
Problem Link: https://leetcode.com/problems/subtree-of-another-tree/

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a 
subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. 
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        
        if self.is_same(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
        
    def is_same(self, root1, root2):
        if not root1 or not root2:
            return root1 == root2
        
        return root1.val == root2.val and self.is_same(root1.left, root2.left) and self.is_same(root1.right, root2.right)


class Solution1:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return s == t
        
        stack = [s]
        while stack:
            node = stack.pop()
            
            if node.val == t.val:
                if self.is_same(node, t):
                    return True
                
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
        
        
    def is_same(self, root1, root2):
        if not root1 or not root2:
            return root1 == root2
        
        return root1.val == root2.val and self.is_same(root1.left, root2.left) and self.is_same(root1.right, root2.right)