"""
Problem Link: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      if not strs:
        return ""
      res = strs[0]
      length = len(res)
      for i in range(1,len(strs)):
        index = 0
        while index < length and index < len(strs[i]):
          if res[index] != strs[i][index]:
            break
          index += 1
        if not index:
          return ""
        length = index
      return res[:length]