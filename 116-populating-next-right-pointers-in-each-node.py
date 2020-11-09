"""
Problem Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, 
the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Note:
You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
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
        
    
    def dfs(self, root, next_node=None):
        if not root:
            return
        
        root.next = next_node
        self.dfs(root.left, root.right)
        self.dfs(root.right, root.next.left if root.next else None)


class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        self.dfs(root)
        return root
        
    
    def dfs(self, root, parent=None):
        if not root:
            return
        
        cur = None
        while parent:
            parent.left.next = parent.right
            if not cur:
                cur = parent.right
            else:
                cur.next = parent.left
                cur = parent.right
            parent = parent.next
            
        self.dfs(root.left, root)

class Solution2:
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
        

class Solution3:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        current = [root] if root else []
        while current:
            nex = []
            prev = None
            for n in current:
                if prev:
                    prev.next = n
                prev = n
                if n.left:
                    nex.append(n.left)
                if n.right:
                    nex.append(n.right)
            current = nex