"""
Problem Link: https://leetcode.com/problems/determine-if-two-strings-are-close/

Two strings are considered close if you can attain one from the other using the following operations:
Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the 
other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.
Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Example 4:
Input: word1 = "cabbba", word2 = "aabbss"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any amount of operations.
 
Constraints:
1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        letters1 = [0] * 26
        letters2 = [0] * 26
        for word in word1:
            letters1[ord(word) - ord('a')] += 1
        
        for word in word2:
            letters2[ord(word) - ord('a')] += 1
            
        
        count = {}
        for i in range(len(letters1)):
            if letters1[i]:
                if letters1[i] in count and letters1[count[letters1[i]]]:
                    count.pop(letters1[i])
                else:
                    count[letters1[i]] = i
            if letters2[i]:
                if letters2[i] in count and letters2[count[letters2[i]]]:
                    count.pop(letters2[i])
                else:
                    count[letters2[i]] = i

        return False if count else True
