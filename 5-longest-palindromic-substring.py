"""
Problem Link: https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
      res = ""
      for i in range(len(s)):
        # self.helper(s,i,i) for cases like # aba
        # self.helper(s,i,i+1) for cases like # abba  
        res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
      return res
       
        
    def helper(self,s,l,r):
      while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
      return s[l+1:r]
