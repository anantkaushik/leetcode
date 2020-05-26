"""
Problem Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Given a string s and an integer k.
Return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are (a, e, i, o, u).

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Example 4:
Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.

Example 5:
Input: s = "tryhard", k = 4
Output: 1
 
Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        cur_max = max_vowels = 0
        
        for i in range(len(s)):
          if s[i] in vowels:
            cur_max += 1
          
          if i >= k and s[i-k] in vowels:
            cur_max -= 1
            
          max_vowels = max(max_vowels, cur_max)
        
        return max_vowels
