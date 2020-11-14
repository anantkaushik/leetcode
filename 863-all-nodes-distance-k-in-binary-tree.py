"""
Problem Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

We are given a binary tree (with root node root), a target node, and an integer value K.
Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 
Note:
The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.parent = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.set_parent(root)
        self.res = []
        self.visited = set()
        self.find_nodes(target, K)
        return self.res
        
        
    def set_parent(self, root, parent=None):
        if not root:
            return 
        
        root.parent = parent
        
        self.set_parent(root.left, root)
        self.set_parent(root.right, root)
    
    def find_nodes(self, node, K):
        if not node or node in self.visited:
            return
        
        self.visited.add(node)
        
        if not K:
            self.res.append(node.val)
            return
        
            
        self.find_nodes(node.left, K-1)
        self.find_nodes(node.right, K-1)
        self.find_nodes(node.parent, K-1)
