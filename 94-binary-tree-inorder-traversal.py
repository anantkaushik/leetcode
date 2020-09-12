"""
Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal/description

Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        res = []
        cur = root
        while cur != None:
            if cur.left == None:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right != None:
                    pre = pre.right
                pre.right = cur
                cur.left, cur = None, cur.left
        return res

class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        if not root:
            return res
        
        stack = []
        cur = root 
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                res.append(node.val)
                cur = node.right
        return res

class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        if not root:
            return res
        
        stack = [root]
        
        while stack:
            if stack[-1].left:
                stack.append(stack[-1].left)
            else:
                node = stack.pop()
                res.append(node.val)
                while stack or node.right:
                    if node.right:
                        stack.append(node.right)
                        break
                    else:
                        node = stack.pop()
                        res.append(node.val)
        return res

class Solution3:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def helper(root):
            if not root:
                return 
            
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        
        helper(root)
        return res