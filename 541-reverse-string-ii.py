"""
Problem Link: https://leetcode.com/problems/reverse-string-ii/

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the 
start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but 
greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = []
        n = len(s)
        revFlag = 1
        i = 0
        while i < n:
            last = min(i + k, n)  
            if revFlag:
                if i > 0:
                    res.append(s[(last-1):(i-1):-1])
                else:
                    res.append(s[(last-1)::-1])
            else:
                res.append(s[i:last])
            revFlag = 1 - revFlag
            i += k
        return "".join(res)