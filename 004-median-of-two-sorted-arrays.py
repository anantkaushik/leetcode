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
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        x,y = len(nums1),len(nums2)
        print(x,y)
        low, high = 0,x
        while low <= high:
            partitionX = (low+high)//2
            partitionY = ((x+y+1)//2) - partitionX
            if partitionX < x and nums2[partitionY-1] > nums1[partitionX]:
                low = partitionX + 1
            elif partitionX > 0 and nums1[partitionX-1] > nums2[partitionY]:
                high = partitionX - 1
            else:
                if partitionX == 0:
                    maxLeft = nums2[partitionY-1]
                elif partitionY == 0:
                    maxLeft = nums1[partitionX-1]
                else:
                    maxLeft = max(nums1[partitionX-1],nums2[partitionY-1])
                if (x+y) % 2 == 1:
                    return maxLeft
                
                if partitionX == x:
                    minRight = nums2[partitionY]
                elif partitionY == y:
                    minRight = nums1[partitionX]
                else:
                    minRight = min(nums1[partitionX],nums2[partitionY])
                return (maxLeft+minRight)/2