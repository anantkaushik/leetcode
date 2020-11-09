"""
Problem Link: https://leetcode.com/problems/binary-tree-postorder-traversal/

Given the root of a binary tree, return the postorder traversal of its nodes' values.
Follow up: Recursive solution is trivial, could you do it iteratively?

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [2,1]
 
Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def helper(root):
            if not root:
                return
            
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        
        helper(root)
        return res

class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        if not root:
            return res
        
        stack = [root]
        visited = set()
        
        while stack:
            if stack[-1].left and stack[-1].left not in visited:
                stack.append(stack[-1].left)
            elif stack[-1].right and stack[-1].right not in visited:
                stack.append(stack[-1].right)
            else:
                node = stack.pop()
                visited.add(node)
                res.append(node.val)
        return res

class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        if not root:
            return res
        
        stack = [root]
        last_node_pushed = None
        
        while stack:
            
            can_visit_left = not (last_node_pushed and last_node_pushed in [stack[-1].left, stack[-1].right])
            
            if stack[-1].left and can_visit_left:
                stack.append(stack[-1].left)
            elif stack[-1].right and stack[-1].right != last_node_pushed:
                    stack.append(stack[-1].right)
            else:
                node = stack.pop()
                last_node_pushed = node
                res.append(node.val)

        return res

class Solution3:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        
        stack, res = [], []
        cur = root
        
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack[-1].right
                if not node:
                    node = stack.pop()
                    res.append(node.val)
                    
                    while stack and stack[-1].right == node:
                        node = stack.pop()
                        res.append(node.val)
                else:
                    cur = node
                         
        return res
