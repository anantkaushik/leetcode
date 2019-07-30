"""
Problem Link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [[root]]
        maxValues = []
        while len(queue) > 0:
            level = queue.pop(0)
            maxNo = float('-inf')
            nextLevel = []
            while len(level) > 0:
                node = level.pop(0)
                if node.val > maxNo:
                    maxNo = node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            maxValues.append(maxNo)
            if len(nextLevel) > 0:
                queue.append(nextLevel)
        return maxValues
        