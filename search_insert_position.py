"""Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Sample Test Cases:
Input: [1,3,5,6], 5
Output: 2
Input: [1,3,5,6], 2
Output: 1
Input: [1,3,5,6], 7
Output: 4
Input: [1,3,5,6], 0
Output: 0
"""
class Solution:
    def binarysearch(self,nums,target):
        first = 0
        last = len(nums)-1
        middle = int((first+last)/2)
        while first<= last:
            if nums[middle] < target:
                first = middle + 1
            elif nums[middle] == target:
                return middle
            else:
                last = middle - 1
            middle = int((first+last)/2)
            if first > last:
                return first
                
    def searchInsert(self, nums, target):
        p = self.binarysearch(nums, target)
        return p