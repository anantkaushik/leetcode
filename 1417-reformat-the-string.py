"""
Problem Link: https://leetcode.com/problems/reformat-the-string/

Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase 
English letters and digits).
You have to find a permutation of the string where no letter is followed by another 
letter and no digit is followed by another digit. That is, no two adjacent characters 
have the same type.
Return the reformatted string or return an empty string if it is impossible to reformat the string.
Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", 
"0a1b2c", "0c2a1b" are also valid permutations.

Example 2:
Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.

Example 3:
Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.

Example 4:
Input: s = "covid2019"
Output: "c2o0v1i9d"

Example 5:
Input: s = "ab123"
Output: "1a2b3"
 
Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""
class Solution:
    def reformat(self, s: str) -> str:
        i = j = 0
        res = []
        count_digit = count_alphabet = 0
        for c in s:
          if 'a' <= c <= 'z':
            count_alphabet += 1
          else:
            count_digit += 1
        if abs(count_digit - count_alphabet) > 1:
          return ""
        
        while i < len(s) and j < len(s):
          while i < len(s) and s[i].isdigit():
            i += 1
          while j < len(s) and 'a' <= s[j] <= 'z':
            j += 1
          if i < len(s) and len(res) % 2 == 0:
            res.append(s[i])
            i += 1
          if j < len(s) and len(res) % 2 != 0:
            res.append(s[j])
            j += 1
        
        if len(res) != len(s):
          if j < len(s):
            res.insert(0, s[j])
          else:
            res.append(s[i])
        return "".join(res)
