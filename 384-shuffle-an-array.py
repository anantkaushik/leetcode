"""
Problem Link: https://leetcode.com/problems/shuffle-an-array/description/

Shuffle a set of numbers without duplicates.

Example:
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);
// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();
// Resets the array back to its original configuration [1,2,3].
solution.reset();
// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
import random
class Solution(object):
    
    def __init__(self, nums):
        self.original = nums
        self.cur = list(nums)
        
    def reset(self):
        self.cur = list(self.original)
        return self.cur
        
    def shuffle(self):
        for i in range(1,len(self.cur)):
            n = random.randint(0,i)
            self.cur[i],self.cur[n] = self.cur[n],self.cur[i]
        return self.cur
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()