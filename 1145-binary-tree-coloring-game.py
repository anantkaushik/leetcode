"""
Problem Link: https://leetcode.com/problems/binary-tree-coloring-game/

Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of 
nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.
Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n 
and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue.
Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color 
(red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, 
right child, or parent of the chosen node.)
If (and only if) a player cannot choose such a node in this way, they must pass their turn.  
If both players pass their turn, the game ends, and the winner is the player that colored more nodes.
You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.  
If it is not possible, return false.

Example 1:
Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
Output: true
Explanation: The second player can choose the node with value 2.
 
Constraints:
root is the root of a binary tree with n nodes and distinct node values from 1 to n.
n is odd.
1 <= x <= n <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.res = None
        self.helper(root, x)
        l, r = self.res
        return ((1 + r + l) < (n - (1 + r + l))) or ((n - max(l,r) - 1) < max(l,r))
        
    def helper(self, root, x):
        if not root or self.res:
            return 0
        
        l = self.helper(root.left, x)
        r = self.helper(root.right, x)
        
        if root.val == x:
            self.res =  [l, r]
            return 0
        
        return 1 + l + r


class Solution1:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.res = None
        self.helper(root, x)
        l, r = self.res
        print(l, r)
        if (1 + r + l) < (n - (1 + r + l)): 
            return True
        elif (n - r - 1) < r:
            return True
        elif (n - l - 1) < l:
            return True
        else:
            return False
        
        
    def helper(self, root, x):
        if not root:
            return 0
        
        l = self.helper(root.left, x)
        r = self.helper(root.right, x)
        
        if root.val == x:
            self.res =  [l, r]
        
        return 1 + l + r