"""
Problem Link: https://leetcode.com/problems/count-sorted-vowel-strings/

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045
 
Constraints:
1 <= n <= 50 Solution:
    def countVowelStrings(self, n: int) -> int:
        self.count = 0
        max_vowels = 5
        
        def helper(n, i, vowel_index):
            if i == n or vowel_index == max_vowels:
                return
            
            self.count += (max_vowels - vowel_index)
            for j in range(i+1, n):
                for k in range(vowel_index + 1, max_vowels):
                    helper(n, j, k)
        
        helper(n, 0, 0)
      
"""
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1] * 6] + [[0] * 6 for i in range(n)]
        
        for i in range(1, n+1):
            for k in range(1, 6):
                dp[i][k] = dp[i][k - 1] + dp[i - 1][k]
                
        return dp[n][5]
    

class Solution1:
    def countVowelStrings(self, n: int) -> int:
        seen = {}
        
        def helper(n, k):
            if n == 1 or k == 1:
                return k
            
            if (n, k) in seen:
                return seen [n, k]
            
            seen[n, k] = sum(helper(n-1, i) for i in range(1, k+1))
            return seen[n, k]
        
        return helper(n, 5)

    
class Solution2:
    def countVowelStrings(self, n: int) -> int:
        a = e = i = o = u = 1
        
        for _ in range(1, n):
            a = a + e + i + o + u
            e = e + i + o + u
            i = i + o + u
            o = o + u
            u = u
        
        return a + e + i + o + u


class Solution3:
    def countVowelStrings(self, n: int) -> int:
        self.count = 0
        max_vowels = 5
        
        def helper(n, i, vowel_index):
            if i == n or vowel_index == max_vowels:
                return
            
            self.count += (max_vowels - vowel_index)
            for j in range(i+1, n):
                for k in range(vowel_index + 1, max_vowels):
                    helper(n, j, k)
        
        helper(n, 0, 0)
        return self.count
