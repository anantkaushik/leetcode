"""
Problem Link: https://leetcode.com/problems/cousins-in-binary-tree/

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 
Constraints:
The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        def helper(root, parent, level, values, parents):
            if len(parents) == 2:
                # print(parents)
                
                return parents[0][0] != parents[1][0] and parents[0][1] == parents[1][1] 
            if not root:
                return False
            
            if root.val in values:
                parents.append((parent, level))
            
            a = helper(root.left, root, level+1, values, parents)
            b = helper(root.right, root, level+1, values, parents)
            return a or b
        
        return helper(root, None, 0, [x,y], [])

        
class Solution1:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent = parent = None
        queue = [[root]]
        while queue:
          level = queue.pop(0)
          next_level = []
          while level:
            node = level.pop()
            if node.left:
              if node.left.val in [x,y]:
                if parent:
                  return parent != node.val
                parent = node.val
              
              next_level.append(node.left)
              
            if node.right:
              if node.right.val in [x,y]:
                if parent:
                  return parent != node.val
                parent = node.val
              
              next_level.append(node.right)
            
          if next_level:
            queue.append(next_level)
          
          if parent:
            return False
        return False


class Solution2:
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        lookUp = {}
        def dfs(root,depth=0,parent=None):
            if not root:
                return None
            if root.val in (x,y): lookUp[root.val] = (depth,parent)
            dfs(root.left,depth + 1, root.val)
            dfs(root.right,depth + 1, root.val)            
        dfs(root)
        return lookUp[x][0] == lookUp[y][0] and lookUp[x][1] != lookUp[y][1]