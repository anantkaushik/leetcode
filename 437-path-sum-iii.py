"""
Problem Link: https://leetcode.com/problems/path-sum-iii/

You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.res = 0
        self.cache = {0: 1}
        self.helper(root, target)
        return self.res
    
    def helper(self, root, target, cur_sum=0):
        if not root:
            return 
        # print(root.val, cur_sum , self.cache)
        cur_sum += root.val
        diff = cur_sum - target
        
        if self.cache.get(diff, 0):
            self.res += self.cache.get(diff)
            
        self.cache[cur_sum] = self.cache.get(cur_sum, 0) + 1
        
        self.helper(root.left, target, cur_sum)
        self.helper(root.right, target, cur_sum)
        self.cache[cur_sum]  -= 1
    
class Solution1:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        ways = self.calculate_ways(root, sum)
        return ways + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def calculate_ways(self, root, sum, cur_sum = 0):
        if not root:
            return 0
        cur_sum += root.val
        val = 1 if cur_sum == sum else 0
        return val + self.calculate_ways(root.left, sum, cur_sum) + self.calculate_ways(root.right, sum, cur_sum) 

class Solution2:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.helper(root,sum,0,{0:1})
        return self.result
    
    def helper(self, root, target, currPathSum, cache):
        if not root:
            return
        complement = currPathSum + root.val - target
        if complement in cache:
            self.result += cache[complement]
        cache.setdefault(currPathSum + root.val, 0)
        cache[currPathSum + root.val] += 1
        self.helper(root.left, target, currPathSum + root.val, cache)
        self.helper(root.right, target, currPathSum + root.val, cache)
        cache[currPathSum + root.val] -= 1
