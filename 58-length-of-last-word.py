"""
Problem Link: https://leetcode.com/problems/length-of-last-word/
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        
        index = len(s) - 1
        while index >= 0:
            if s[index] != "":
                return len(s[index])
            index -= 1


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        count = 0
        flag = False
        while index >= 0:
            if flag:
                if s[index] == ' ':
                    return count
                count += 1
            elif s[index] != ' ':
                flag = True
                count += 1
            
            index -= 1
        
        return count
