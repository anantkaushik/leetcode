"""
Problem Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        def helper(root, level=0):
            if not root:
                return
            
            if len(res) == level:
                res.append([])
            
            helper(root.left, level+1)
            helper(root.right, level+1)
            if not level % 2:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
        
        helper(root)
        return res


class Solution1:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        depth = 1
        level = [root]
        while level:
            new_level = []
            cur_level = []
            flag = depth % 2
            for node in level:
                if flag:
                    cur_level.append(node.val)
                else:
                    cur_level.insert(0, node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
                
            level = new_level if new_level else None
            res.append(cur_level)
            depth += 1
        
        return res