"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""
class Solution(object):
    def isValid(self, s):
        l = len(s)
        if l == 0:
            return True
        valid_parentheses = ['()','{}','[]']
        stack = list()
        stack.append(s[0])
        for i in range(1,l):
            if stack:
                last = stack.pop()
                check = last + s[i]
                if check not in valid_parentheses:
                    stack.append(last)
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return False if stack else True