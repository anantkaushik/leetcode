"""
Problem Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Given a binary tree
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be 
set to NULL.
Initially, all next pointers are set to NULL.

Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 
Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its 
next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, 
with '#' signifying the end of each level.
 
Constraints:
The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        self.dfs(root)
        return root
        
    
    def dfs(self, root, parent=None):
        if not root:
            return
        cur1 = cur2 = None
        while parent:
            
            if not parent.left and not parent.right:
                parent = parent.next
                continue
                
            if not cur1:
                cur1 = parent.left or parent.right
                if cur1 == parent.right:
                    parent = parent.next
                    
            elif not cur2:
                if cur1 == parent.right or cur1 == parent.left and not parent.right:
                    parent = parent.next
                    continue
                if cur1 == parent.left:
                    cur2 = parent.right
                else:
                    cur2 = parent.left or parent.right
                    
            else:
                cur1.next = cur2
                cur1, cur2 = cur2, None
            
        self.dfs(root.left, root)
        self.dfs(root.right, root)
        
        
class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        self.dfs(root)
        return root
        
    
    def dfs(self, root, next_node=None):
        if not root:
            return
        
        root.next = next_node
        
        n1 = root.right
        n2 = root.next.left if root.next else None
        n3 = root.next.right if root.next else None 
        next_node = n1 or n2 or n3
        if root.left:
            self.dfs(root.left, next_node)
        if root.right:
            if next_node == n1:
                next_node = n2 or n3
            elif next_node == n2:
                next_node = n3
            else:
                next_node = None
            self.dfs(root.right, next_node)
