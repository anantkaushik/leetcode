"""
Problem Link: https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i,j = len(S) - 1, len(T) - 1
        s_skip = t_skip = 0
        while i >= 0 or j >= 0:
          while i >= 0:
            if S[i] == '#':
              s_skip += 1
              i -= 1
            elif s_skip > 0:
              s_skip -= 1
              i -= 1
            else:
              break
              
          while j >= 0:
            if T[j] == '#':
              t_skip += 1
              j -= 1
            elif t_skip > 0:
              t_skip -= 1
              j -= 1
            else:
              break
          
          if i >= 0 and j >= 0 and S[i] != T[j]:
            return False
          
          if (i >= 0) != (j >=0):
            return False
          i -= 1
          j -= 1
        return True

# Short Solution 
class Solution1:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i,j = len(S) - 1, len(T) - 1
        s_skip = t_skip = 0
        while i >= 0 or j >= 0:
          while i >= 0 and (s_skip or  S[i] == '#'):
            s_skip += 1 if S[i] == '#' else -1
            i -= 1
              
          while j >= 0 and (t_skip or T[j] == '#'):
            t_skip += 1 if T[j] == '#' else -1
            j -= 1
          
          if not (i >= 0 and j >= 0 and S[i] == T[j]):
            return i == j == -1
          i -= 1
          j -= 1
        return True