"""
Problem Link: https://leetcode.com/problems/longest-happy-string/

A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.
Given three integers a, b and c, return any string s, which satisfies following conditions:
s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 2, b = 2, c = 1
Output: "aabbc"

Example 3:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.
 
Constraints:
0 <= a, b, c <= 100
a + b + c > 0
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        values = [a, b, c]
        old_values = [a,b,c]
        max_value = max(values)
        index = values.index(max_value)
        
        while max_value:
          if max_value >= 2 and (max(old_values) - max_value <= 2) :
            old_values = [value for value in values]
            res.append(chr(index + ord('a')) * 2)
            values[index] -= 2
          else:
            old_values = [value for value in values]
            res.append(chr(index + ord('a')))
            values[index] -= 1
            
          if index == 0:
            max_value = values[1] if values[1] > values[2] else values[2]
            index = 1 if values[1] > values[2] else 2
          elif index == 1:
            max_value = values[0] if values[0] > values[2] else values[2]
            index = 0 if values[0] > values[2] else 2
          else:
            max_value = values[0] if values[0] > values[1] else values[1]
            index = 0 if values[0] > values[1] else 1
            
            
        return "".join(res)
