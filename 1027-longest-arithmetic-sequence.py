"""
Problem Link: https://leetcode.com/problems/longest-arithmetic-sequence/

Given an array A of integers, return the length of the longest arithmetic subsequence in A.
Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 
0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] 
are all the same value (for 0 <= i < B.length - 1).

Example 1:
Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.

Example 2:
Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].

Example 3:
Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].
 
Note:
2 <= A.length <= 2000
0 <= A[i] <= 10000
"""
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
import collections
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = collections.defaultdict(dict)
        maxLength = 1
        for i in range(1,len(A)):
          for j in range(i):
            diff = A[i] - A[j]
            dp[i][diff] = 1 + dp[j].get(diff, 1)
            maxLength = max(maxLength, dp[i][diff])
        return maxLength

class Solution1:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
          for j in range(i+1, len(A)):
            diff = A[j] - A[i]
            dp[j, diff] = dp.get((i, diff), 1) + 1
        return max(dp.values())