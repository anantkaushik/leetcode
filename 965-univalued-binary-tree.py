"""
Problem Link: https://leetcode.com/problems/univalued-binary-tree/

A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.

Example 1:
Input: [1,1,1,1,1,null,1]
Output: true

Example 2:
Input: [2,2,2,5,2]
Output: false
 
Note:
The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = [root]
        val = root.val
        while q:
            temp = q.pop(0)
            if temp.val != val:
                return False
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return True