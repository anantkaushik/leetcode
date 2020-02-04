"""
Problem Link: https://leetcode.com/problems/score-of-parentheses/

Given a balanced parentheses string S, compute the score of the string based on the following rule:
() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 
Example 1:
Input: "()"
Output: 1

Example 2:
Input: "(())"
Output: 2

Example 3:
Input: "()()"
Output: 2

Example 4:
Input: "(()(()))"
Output: 6
 
Note:
S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
      res = bal = 0
      for i in range(len(S)):
        bal += 1 if S[i] == '(' else -1
        if S[i] == ')' and S[i-1] == '(':
          res += 2**bal
      return res

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution1:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for c in S:
          if c == '(':
            stack.append(0)
          else:
            last_element = stack.pop()
            stack[-1] += max(2*last_element, 1)
        return stack.pop()
            
class Solution2:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for parentheses in S:
          if parentheses == '(':
            stack.append('(')
          else:
            last_element = stack.pop()
            if last_element == '(':
              stack.append(1)
            else:
              stack.pop()
              stack.append(last_element*2)
          self.getSum(stack)
        return stack[0]
          
    def getSum(self, stack):
      if stack and stack[-1] == '(':
        return
      res = 0
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.append(res)
            