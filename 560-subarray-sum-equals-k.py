"""
Problem Link: https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count,summ,d = 0,0,{0:1}
        for n in nums:
            summ += n
            if summ - k in d:
                count += d[summ-k]
            d[summ] = d.get(summ,0) + 1
        return count