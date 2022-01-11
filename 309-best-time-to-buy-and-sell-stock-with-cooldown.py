"""
Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        """
        Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75931/Easiest-JAVA-solution-with-explanations
        buy[i] = Math.max(buy[i - 1], sell[i - 2] - prices[i]);   
        sell[i] = Math.max(sell[i - 1], buy[i - 1] + prices[i]);
        
        Let b2, b1, b0 represent buy[i - 2], buy[i - 1], buy[i]
        Let s2, s1, s0 represent sell[i - 2], sell[i - 1], sell[i]
        Then arrays turn into Fibonacci like recursion:

        b0 = Math.max(b1, s2 - prices[i]);
        s0 = Math.max(s1, b1 + prices[i]);
        """
        b0 = b1 = -prices[0]
        s0 = s1 = s2 = 0
        
        for i in range(1, len(prices)):
            b0 = max(b1, s2 - prices[i])
            s0 = max(s1, b1 + prices[i])
            b1, s1, s2 = b0, s0, s1
        
        return s0
