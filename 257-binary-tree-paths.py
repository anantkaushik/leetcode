"""
Problem Link: https://leetcode.com/problems/binary-tree-paths/

Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1:

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        return self.helper(root, [], [])
    
    def helper(self, root, res, cur_path):
        if not root:
            return res
        
        cur_path.append(str(root.val))
        if not root.left and not root.right:
            res.append("->".join(cur_path))
            
        self.helper(root.left, res, cur_path)
        self.helper(root.right, res, cur_path)
        cur_path.pop()
        return res
