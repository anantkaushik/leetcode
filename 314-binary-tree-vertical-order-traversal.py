"""
Problem Link: https://leetcode.com/problems/binary-tree-vertical-order-traversal/

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

Examples 1:
Input: [3,9,20,null,null,15,7]
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:
[
  [9],
  [3,15],
  [20],
  [7]
]

Examples 2:
Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]

Examples 3:
Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        self.d = {}
        self.bfs(root)
        
        res = []
        for x in sorted(self.d.keys()):
            res.append(self.d[x])
        
        return res
    
    def bfs(self, root):
        if not root:
            return 
        
        stack = [[root, 0]]
        while stack:
            new_level = []
            temp = []
            for i in range(len(stack)):
                node, x = stack[i]
                if node.left:
                    new_level.append([node.left, x-1])
                if node.right:
                    new_level.append([node.right, x+1])
                    
                if x in self.d:
                    self.d[x].append(node.val)
                else:
                    self.d[x] = [node.val]
                
            stack = new_level if new_level else None
