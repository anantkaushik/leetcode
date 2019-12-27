"""
Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    # Time Complexity: O(2N) = O(N)
    # Space Complexity: O(min(m, n)). We need O(k) space for the sliding window, 
        # where k is the size of the Set. The size of the Set is upper bounded by the 
        # size of the string n and the size of the charset/alphabet m
    def lengthOfLongestSubstring(self, s: str) -> int:
      temp = set()
      max_length = 0
      index = 0
      for i in range(len(s)):
        if s[i] in temp:
          max_length = max(max_length, i-index)
          while s[index] != s[i]:
            temp.remove(s[index])
            index += 1
          index += 1
        else:
          temp.add(s[i])
      return max(max_length, len(s)-index)

    # Time Complexity : O(N)
    # Space Complexity: O(k)
    def lengthOfLongestSubstring1(self, s: str) -> int:
      d = {}
      max_length = 0
      lower_limit = 0
      for i in range(len(s)):
        if s[i] in d:
          lower_limit = max(d.get(s[i]), lower_limit)
        max_length = max(max_length, i - lower_limit  + 1)
        d[s[i]] = i + 1
      return max_length