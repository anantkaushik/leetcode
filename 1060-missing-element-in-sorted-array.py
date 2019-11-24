"""
Given a sorted array A of unique numbers, 
find the K-th missing number starting from the leftmost number of the array.

Example 1:
Input: A = [4,7,9,10], K = 1
Output: 5
Explanation:
    The first missing number is 5.

Example 2:
Input: A = [4,7,9,10], K = 3
Output: 8
Explanation:
    The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:
Input: A = [1,2,4], K = 3
Output: 6
Explanation:
    The missing numbers are [3,5,6,7,...], hence the third missing number is 6.


Note:
1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
"""
class Solution:
    # Time O(logn) and Space O(1)
    def missingElement(self, nums, k):
        mis = self.missing(nums, len(nums)-1)
        if mis < k:
            return nums[-1] + (k- mis)

        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start+end)//2
            mis = self.missing(nums, mid)
            if mis < k:
            # We can't choose <= K because
            # it says, it's a potential answer let's keep it and 
            # see if we can find bigger answer
            # we will maximize the result which is not what we want
                start = mid + 1
            else:
                end = mid

        return nums[start-1] + (k-self.missing(nums, start - 1))


    def missing(self, nums, index):
        # K = actual present - should be present
        return nums[index]- (nums[0] + index)


class solution:
    # Time O(n) and Space O(1)
    def missingElement(self, nums, k):
        index = 0
        for i in range(nums[0], nums[-1]+1):
            if nums[index] == i:
                index += 1
            else:
                k -= 1
            if k == 0:
                return i
        while k:
            i += 1
            k -= 1
        return i