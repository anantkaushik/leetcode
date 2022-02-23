"""
Problem Link: https://leetcode.com/problems/find-leaves-of-binary-tree/

Given the root of a binary tree, collect a tree's nodes as if you were doing this:
Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per 
each level it does not matter the order on which elements are returned.

Example 2:
Input: root = [1]
Output: [[1]]

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
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = []
        self.get_height(root, leaves)
        return leaves
    
    def get_height(self, root, leaves):
        if not root:
            return -1
        
        height = 1 + max(self.get_height(root.left, leaves),
                         self.get_height(root.right, leaves))
        if height > len(leaves) - 1:
            leaves.append([])
        
        leaves[height].append(root.val)
        
        return height
