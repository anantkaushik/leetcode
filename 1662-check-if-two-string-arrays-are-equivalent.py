"""
Problem Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
 
Constraints:
1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
"""
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i = j = inner_i = inner_j = 0
        while i < len(word1) and j < len(word2):
            if word1[i][inner_i] != word2[j][inner_j]:
                return False
            
            if inner_i + 1 == len(word1[i]):
                inner_i = 0 
                i += 1
            else:
                inner_i += 1
                
            if inner_j + 1 == len(word2[j]):
                inner_j = 0 
                j += 1
            else:
                inner_j += 1
        
        return i >= len(word1) and j >= len(word2)