"""
Problem Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parents = {root: None}
        given_nodes = [p,q]

        while stack:
            node = stack.pop()
            
            if node in given_nodes:
                given_nodes.remove(node)
                if not given_nodes:
                    break
                continue
            
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
            
            if node.left:
                parents[node.left] = node
                stack.append(node.left)

        if not p in parents or not q in parents:
            return p if p in parents else q

        q_parents = self.get_parents(parents, q)
        p_parents = self.get_parents(parents, p)

        return self.get_parent(p_parents, q_parents)
        
    def get_parents(self, parents, node):
        res = []
        while node:
            if parents[node]:
                res.append(parents[node])
            node = parents[node]
        return res
    
    def get_parent(self, p_parents, q_parents):
        i, j = len(p_parents)-1, len(q_parents)-1
        
        while i >= 0 and j >= 0 and p_parents[i] == q_parents[j]:
            i -= 1
            j -= 1
        return p_parents[i+1]



class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 
        
        if root in [p,q]:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        
        if l and r:
            return root
        
        return  l or r