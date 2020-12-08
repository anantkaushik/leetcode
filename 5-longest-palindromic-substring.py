"""
Problem Link: https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        new_s = '#'.join('^{}$'.format(s))
        n = len(new_s)
        p = [0] * n
        c = r = 0
        
        for i in range (1, n-1):
            if i < r:
                mirr = 2*c - i # equals to i' = C - (i-C)
                p[i] = min(r - i, p[mirr]) 
                
            while new_s[i + 1 + p[i]] == new_s[i - 1 - p[i]]:
                p[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + p[i] > r:
                c, r = i, i + p[i]
    
        maxLen, centerIndex = max((n, i) for i, n in enumerate(p))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]


class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        self.start_index = self.max_len = -1
        
        for i in range(len(s)):
            self.find_palindrome(s, i, i)
            self.find_palindrome(s, i, i+1)
        
        return s[self.start_index: self.start_index + self.max_len]
    
    def find_palindrome(self, s, left_index, right_index):
        while left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]:
            left_index -= 1
            right_index += 1
        if self.max_len < right_index - left_index -1:
            self.start_index = left_index + 1
            self.max_len = right_index - left_index - 1


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        dp = [[False] * len(s) for _ in range(len(s))]
        
        start_index = max_len = 0
        for i in range(len(s)):
            for j in range(i+1):
                dp[j][i] = ((s[i]==s[j]) and (i-j<=2 or dp[j+1][i-1]))
                
                if dp[j][i] and i - j + 1 > max_len:
                    max_len = i - j + 1
                    start_index = j
                    
        return s[start_index: start_index + max_len]
        

class Solution3:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        start_index = max_len = 0
        for i in range(len(s)):
            for j in range(len(s)-1, i-1, -1):
                if s[i:j+1] == (s[j:i-1:-1] if i > 0 else s[j::-1]):
                    if max_len < j - i + 1:
                        start_index = i
                        max_len = j - i + 1
                    break
        return s[start_index: start_index + max_len]
            