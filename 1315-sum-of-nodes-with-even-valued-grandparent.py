"""
Problem Link: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

Given a binary tree, return the sum of values of nodes with even-valued grandparent. 
(A grandparent of a node is the parent of its parent, if it exists.)
If there are no nodes with an even-valued grandparent, return 0.

Example 1:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 
Constraints:
The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def helper(root, parent=None, grand_parent=None):
            if not root:
                return 0
            
            val = root.val if grand_parent and grand_parent.val % 2 == 0 else 0
            
            return val + helper(root.left, root, parent) + helper(root.right, root, parent)
        
        
        return helper(root)

        
class Solution1:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        
        def helper(root, parent=None, grand_parent=None):
            if not root:
                return 0
            
            if grand_parent and grand_parent.val % 2 == 0:
                self.sum += root.val
            
            helper(root.left, root, parent)
            helper(root.right, root, parent)
        
        helper(root)
        return self.sum