"""
Problem Link: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

Given two sparse vectors, compute their dot product.
Implement class SparseVector:
SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse 
vector efficiently and compute the dot product between two SparseVector.
Follow up: What if only one of the vectors is sparse?

Example 1:
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

Example 2:
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

Example 3:
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6

Constraints:
n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100
"""
class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeroes = []
        for index, num in enumerate(nums):
            if num != 0:
                self.non_zeroes.append([index, num])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        prod = 0
        index1 = index2 = 0
        
        while index1 < len(self.non_zeroes) and index2 < len(vec.non_zeroes):
            if self.non_zeroes[index1][0] == vec.non_zeroes[index2][0]:
                prod += (self.non_zeroes[index1][1] * vec.non_zeroes[index2][1])
                index1 += 1
                index2 += 1
            elif self.non_zeroes[index1][0] < vec.non_zeroes[index2][0]:
                index1 += 1
            else:
                index2 += 1
        
        return prod

    
class SparseVector1:
    def __init__(self, nums: List[int]):
        self.non_zeroes = {}
        for index, num in enumerate(nums):
            if num != 0:
                self.non_zeroes[index] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        prod = 0
        for index, num in self.non_zeroes.items():
            if index in vec.non_zeroes:
                prod += (vec.non_zeroes[index] * num)
        
        return prod
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
