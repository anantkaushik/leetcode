"""
Problem Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any node sequence from some starting node to any node in the tree along 
the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
Input: root = [1,2,3]
Output: 6

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
 
Constraints:
The number of nodes in the tree is in the range [0, 3 * 104].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        def helper(root):
            if not root:
                return 0
            
            l = max(helper(root.left), 0)
            r = max(helper(root.right), 0)
            cur = root.val
            self.ans = max(self.ans, cur+l+r)
            return cur + max(l, r)
        helper(root)
        return self.ans


class Solution1:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        self.node_max_val = {}
        stack = []
        cur = root
        
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack[-1].right
                if node:
                    cur = node
                else:
                    node = stack.pop()
                    self.set_max(node)
                    while stack and stack[-1].right == node:
                        node = stack.pop()
                        self.set_max(node)
                        
        return self.ans
    
    def set_max(self, node):
        l = self.node_max_val[node.left] if node.left in self.node_max_val else 0
        r = self.node_max_val[node.right] if node.right in self.node_max_val else 0
        
        val = max(node.val + l, node.val + r, node.val)
        self.ans = max(self.ans, val, node.val + l + r)
        self.node_max_val[node] = val