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
import collections
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        letters = collections.defaultdict(int)
        for c in s:
            letters[c] += 1
        for c in t:
            if letters[c] <= 0:
                return False
            letters[c] -= 1
        return True