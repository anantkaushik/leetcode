"""
Problem Link: https://leetcode.com/problems/best-sightseeing-pair/

Given an array A of positive integers, A[i] represents the value of 
the i-th sightseeing spot, and two sightseeing spots i and j have 
distance j - i between them.
The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j): 
the sum of the values of the sightseeing spots, minus the distance between them.
Return the maximum score of a pair of sightseeing spots.

Example 1:
Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 
Note:
2 <= A.length <= 50000
1 <= A[i] <= 1000
"""
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
      startMax = 0
      endMax = 0
      for i in range(len(A)-1):
        startMax = max(startMax, A[i]+i)
        endMax = max(endMax,startMax + A[i+1]-(i+1))
      return endMax

    # It's similar to Best Time to Buy and Sell Stock, 
    # but instead of min price, we track max value (a[i]+i), 
    # and our max value decays every step due to the distance penalty.
    # Solution
    # Track the maximum value of A[i] as max_i.
    # Every turn, decrement max_ito account for j - i.
    # Track and return the maximum score.
    def maxScoreSightseeingPair_alternative(self, A: List[int]) -> int:
      max_i = A[0] - 1
      res = 0
      for j in range(1,len(A)):
        res = max(res,A[j]+max_i)
        max_i = max(max_i, A[j])
        max_i -= 1
      return res