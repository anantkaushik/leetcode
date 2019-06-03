"""
Problem Link: https://leetcode.com/problems/shortest-distance-to-a-character/

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:
S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        prev = float('-inf')
        ans = []
        for i in range(len(s)):
            if s[i] == c:
                prev = i
            ans.append(i-prev)
        
        prev = float('inf')
        for i in range(len(s)-1,-1,-1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i],prev-i)
        
        return ans