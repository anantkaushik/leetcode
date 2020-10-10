"""
Problem Link: https://leetcode.com/problems/divide-chocolate/

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.
You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, 
each piece consists of some consecutive chunks.
Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.
Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

Example 1:
Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]

Example 2:
Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.

Example 3:
Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
 
Constraints:
0 <= K < sweetness.length <= 10^4
1 <= sweetness[i] <= 10^5
"""
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        start, end = min(sweetness), sum(sweetness)//(K+1)
        ans = None 
        while start <= end:
            mid = (start+end)//2
            print(start, end, mid)
            if self.canDivide(sweetness, K+1, mid):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans
                
        
    def canDivide(self, sweetness, k, m):
        cuts, num = 0, 0
        for val in sweetness:
            num += val
            if num >= m:
                cuts += 1
                num = 0
            if cuts >= k:
                return True
        
        return False
