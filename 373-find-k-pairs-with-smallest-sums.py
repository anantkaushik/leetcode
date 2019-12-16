"""
Problem Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u,v) which consists of one element from the first array and one element 
from the second array.
Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""
import heapq
class Solution:
    # Time Complexity: O(lkogk)
    # Space Complexity: O(k) 
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        priorityQueue = []
        res = []
        if not k or not nums1 or not nums2:
          return res
        for i in range(min(len(nums1),k)):
          heapq.heappush(priorityQueue, (nums1[i] + nums2[0], i, 0))
        while k > 0 and priorityQueue:
          k -=  1
          _, i, j = heapq.heappop(priorityQueue)
          res.append([nums1[i], nums2[j]])
          if j < len(nums2)-1:
            heapq.heappush(priorityQueue, (nums1[i] + nums2[j+1], i, j+1))
        return res