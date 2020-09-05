"""
Problem Link: https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.

Example:
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity - O(n), n is the total no of nodes
# Space Complexity - O(n), Because of recursion, O(h) function calls will be placed on the queue 
# in the worst case, where h is the height of the tree. Because h in h ∈ O(n), 
# the space complexity is O(n)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
          return 
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# Time Complexity - O(n), n is the total no of nodes
# Space complexity - O(n), since in the worst case, the queue will contain all nodes in one 
# level of the binary tree. For a full binary tree, the leaf level has n/2 = O(n) leaves.
class SolutionIterative:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
          return 

        queue = []
        queue.append(root)
        
        while queue:
          cur = queue.pop(0)
          cur.left, cur.right = cur.right, cur.left
          if cur.left:
            queue.append(cur.left)
          if cur.right:
            queue.append(cur.right)
        return root