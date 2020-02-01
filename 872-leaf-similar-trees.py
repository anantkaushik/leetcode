"""
Problem Link: https://leetcode.com/problems/leaf-similar-trees/

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:
Both of the given trees will have between 1 and 100 nodes.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leafInorder(root1) == self.leafInorder(root2)
        
    def leafInorder(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.leafInorder(root.left) + self.leafInorder(root.right)


class SolutionIterative:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
      return self.getLeaves(root1) == self.getLeaves(root2)
      
    def getLeaves(self, root):
      stack = [root]
      leaves = []
      while stack:
        node = stack.pop()
        if not node.left and not node.right:
          leaves.append(node.val)
        if node.left:
          stack.append(node.left)
        if node.right:
          stack.append(node.right)
      print(leaves)
      return leaves