"""
Problem Link: https://leetcode.com/problems/kth-missing-positive-number/

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Find the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start, end = 0, len(arr)
        
        while start < end:
            mid = (start+end)//2
            
            if arr[mid] - (mid + 1) < k:
                start = mid + 1
            else:
                end = mid

        return start + k
    
class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[-1] - len(arr) < k:
            return arr[-1] + (k - (arr[-1] - len(arr)))
            
        start, end = 0, len(arr)-1
        
        while start <= end:
            mid = (start+end)//2
            if arr[mid] - (mid + 1) < k:
                start = mid + 1
            else:
                end = mid - 1

        if end == -1:
            num = 0
            missing = 0
        else:
            num = arr[end]
            missing = arr[end] - (end+1)
        return num + (k - missing)
    
class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        index = 0
        num = 1
        while index < len(arr):
            if arr[index] == num:
                index += 1
            else:
                k -= 1
            
            if not k:
                return num
            
            num += 1
        return arr[-1] + k
