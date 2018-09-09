"""
Problem Link: https://leetcode.com/problems/number-of-segments-in-a-string/description

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.

Example:
Input: "Hello, my name is John"
Output: 5
"""
class Solution(object):
    def countSegments(self, s):
        l = s.split()
        return len(l)