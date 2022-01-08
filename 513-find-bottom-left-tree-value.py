"""
Problem Link: https://leetcode.com/problems/find-bottom-left-tree-value/

Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:
Input: root = [2,1,3]
Output: 1

Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 
Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0, [0, root.val])[1]
    
    def helper(self, root, cur_height, res):
        if not root:
            return res
        
        if cur_height > res[0]:
            res[0] = cur_height
            res[1] = root.val
        
        self.helper(root.left, cur_height + 1, res)
        self.helper(root.right, cur_height + 1, res) 
        return res
