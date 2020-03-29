"""
Problem Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""
class Solution:
    # Time Complexity: O(log(min(m,n)))
    # Space Complexity: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if  len(nums1) > len(nums2):
          return self.findMedianSortedArrays(nums2, nums1)
        start = 0
        end = len(nums1)
        while start <= end:
          midX = (start+end)//2
          midY = ((len(nums1) + len(nums2) + 1)//2) - midX
          leftX = float('-inf') if midX == 0 else nums1[midX-1]
          rightX = float('inf') if midX == len(nums1) else nums1[midX]
          
          leftY = float('-inf') if midY == 0 else nums2[midY-1]
          rightY = float('inf') if midY == len(nums2) else nums2[midY]
          if leftX <= rightY and leftY <= rightX:
            if (len(nums1)+len(nums2)) % 2 == 0:
              return (max(leftX, leftY)+min(rightX, rightY))/2
            else:
              return max(leftX, leftY)
            
          elif leftX > rightY:
            end = midX - 1
          else:
            start = midX + 1
