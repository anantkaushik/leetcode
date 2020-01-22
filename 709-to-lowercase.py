"""
Problem Link: https://leetcode.com/problems/to-lower-case/
Implement function ToLowerCase() that has a string parameter str, and returns the same string 
in lowercase.

Example 1:
Input: "Hello"
Output: "hello"

Example 2:
Input: "here"
Output: "here"

Example 3:
Input: "LOVELY"
Output: "lovely"
"""
class Solution:
    def toLowerCase(self, str: str) -> str:
        # return ''.join([chr(ord('a')+ord(s)-ord('A')) if ord(s) <= ord('Z') and ord(s) >= ord('A') else s for s in str])
        return "".join([chr(ord(c)+32) if 65 <= ord(c) <= 90 else c for c in str])
        

