"""
Problem Link: https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = []
        cur = root
        prev = None
        
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                if prev and prev.val >= node.val:
                    return False
                prev = node
                cur = node.right
        return True

class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = [[root, float('-inf'), float('inf')]]
        
        while stack:
            node, min_val, max_val = stack.pop()
            if not node: 
                continue
                
            if not (min_val < node.val < max_val):
                return False
            
            stack.append([node.left, min_val, node.val])
            stack.append([node.right, node.val, max_val])
                
        return True

class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
        
    def helper(self, root, min_val, max_val):
        if not root:
            return True
        
        if min_val < root.val < max_val:
            return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)
        return False

class Solution3:
    def isValidBST(self, root,minn = float('-inf'),maxx = float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val <= minn or root.val >= maxx:
            return False
        if not self.isValidBST(root.right,root.val,maxx):
            return False
        if not self.isValidBST(root.left,minn,root.val):
            return False
        return True