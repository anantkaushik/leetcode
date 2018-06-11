"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""
class Solution(object):
    def firstUniqChar(self, s):
        res = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            i = s.find(c)
            if i != -1 and i == s.rfind(c):
                res = min(res, i)
        return res if res != len(s) else -1