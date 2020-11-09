"""
Problem Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        
        inorder_indexes = {v:i for i, v in enumerate(inorder)}
        
        preorder_index = 1
        root = TreeNode(preorder[0])
        stack = [[root, 0, len(preorder)-1]]
        
        while preorder_index < len(preorder):
            
            node, start, end = stack[-1]
            node_inorder_index = inorder_indexes[node.val]
            cur_val = preorder[preorder_index]
            cur_inorder_index = inorder_indexes[cur_val]
            
            if start <= cur_inorder_index <= end:
                new_node = TreeNode(cur_val)
                
                if cur_inorder_index < node_inorder_index:
                    node.left = new_node
                    stack.append([new_node, start, node_inorder_index-1])
                else:
                    node.right = new_node
                    stack.append([new_node, node_inorder_index+1, end])
                preorder_index += 1
            else:
                stack.pop()
        
        return root

class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        
        self.index = 0
        def helper(start=0, end=len(inorder)-1):
            if start > end:
                return 
            
            root_val = preorder[self.index]
            inorder_index = find_index(root_val, start, end)
            if inorder_index == -1:
                return
            else:
                self.index += 1

            node = TreeNode(root_val) 
            node.left = helper(start, inorder_index-1) 
            node.right = helper(inorder_index+1, end) 
            
            return node
        
        def find_index(root_val, start, end):
            for i in range(start, end+1):
                if inorder[i] == root_val:
                    return i
            return -1
        
        return helper()

class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        
        self.index = 0
        def helper(order):
            if not order:
                return 
            root_val = preorder[self.index]
            inorder_index = find_index(order, root_val)
            if inorder_index == -1:
                return
            else:
                self.index += 1
            
            node = TreeNode(root_val) 
            node.left = helper(order[:inorder_index]) 
            node.right = helper(order[inorder_index+1:]) 
            
            return node
        
        def find_index(arr, val):
            for i in range(len(arr)):
                if arr[i] == val:
                    return i
            return -1
        
        return helper(inorder)
