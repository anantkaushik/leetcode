"""
Problem Link: https://leetcode.com/problems/binary-tree-right-side-view/

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you 
can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        
        def helper(root, level):
            if not root:
                return
            
            if level >= len(res):
                res.append(root.val)
            helper(root.right, level+1)
            helper(root.left, level+1)
        
        helper(root, 0)
        return res


class Solution1:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return
        
        res, queue = [], [root]
        
        while queue:
            new_level = []
            temp_val = None
            
            for node in queue:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            
            res.append(queue[-1].val)
            queue = new_level if new_level else None
        
        return res