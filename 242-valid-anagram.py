"""
Problem Link: https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
# Time Complexity - O(N)
# Space Complexity - O(1) Because maximum size for letters dict is 26
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = {}
        for c in s:
            letters[c] = letters.get(c,0) + 1
        for c in t:
            if letters.get(c,0) <= 0:
                return False
            letters[c] -= 1
        return True