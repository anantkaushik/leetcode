"""
Problem Link: https://leetcode.com/problems/min-cost-climbing-stairs/

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p1, p2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            p1, p2 = p2, cost[i] + min(p1, p2)
        return min(p1, p2)
    
    
class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        for i in range(len(cost)):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])
    
    
class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dp = [0]*len(cost)
        self.dp[0] = cost[0]
        self.dp[1] = cost[1]
        
        return min(self.helper(len(cost)-1, cost), self.helper(len(cost)-2, cost))
        
    def helper(self, staircase, cost):
        if staircase <= 1:
            return self.dp[staircase]
        if self.dp[staircase]:
            return self.dp[staircase]
            
        self.dp[staircase] = cost[staircase] + min(self.helper(staircase-1, cost), self.helper(staircase-2, cost))
        return self.dp[staircase]
    
    
class Solution3:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.helper(len(cost)-1, cost), self.helper(len(cost)-2, cost))
        
    def helper(self, staircase, cost):
        if staircase <= 1:
            return cost[staircase]

        return cost[staircase] + min(self.helper(staircase-1, cost), self.helper(staircase-2, cost))