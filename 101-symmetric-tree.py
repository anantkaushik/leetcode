"""
Problem Link: https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root,root)
    
    def isMirror(self,l,r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val == r.val:
            return self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)
        return False

class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(root1, root2):
            if not root1 or not root2:
                return root1 == root2
            
            return root1.val == root2.val and helper(root1.left, root2.right) and helper(root1.right, root2.left)
        
        return helper(root, root)

class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [[root, root]]
        
        while stack:
            node1, node2 = stack.pop()
            
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            stack.append([node1.left, node2.right])
            stack.append([node1.right, node2.left])
            
        return True