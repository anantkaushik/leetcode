"""
Problem Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        node = root
        while node:
            if node.left:
                nodeL = node.left
                while nodeL.right:
                    nodeL = nodeL.right
                tmp, node.left = node.left, None
                nodeL.right, node.right = node.right, tmp
            node = node.right