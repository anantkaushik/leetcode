"""
Problem Link: https://leetcode.com/problems/maximum-number-of-balloons/

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
 
Constraints:
1 <= text.length <= 10^4
text consists of lower case English letters only.
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        alphabets = [0]*26
        for c in text:
          alphabets[ord(c)-ord('a')] += 1
        return min(alphabets[0],alphabets[1],alphabets[11]//2,alphabets[14]//2,alphabets[13])