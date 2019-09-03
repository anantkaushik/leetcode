"""
Problem Link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

Example 1:
Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
 
Note:
The number of nodes in the given tree is between 1 and 10^4.
-10^5 <= node.val <= 10^5
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = maxLevel = 0
        if not root:
            return maxLevel
        queue = [[root]]
        maxSum = float('-inf')
        while queue:
          level += 1
          levelNodes = queue.pop(0)
          nextLevel = []
          levelSum = 0
          while levelNodes:
            node = levelNodes.pop()
            levelSum +=node.val
            if node.left:
              nextLevel.append(node.left)
            if node.right:
              nextLevel.append(node.right)
          if nextLevel:
            queue.append(nextLevel)
          if levelSum > maxSum:
            maxSum = levelSum
            maxLevel = level
        return maxLevel