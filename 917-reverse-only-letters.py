"""
Problem Link: https://leetcode.com/problems/reverse-only-letters/

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, 
and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 
Note:
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
"""
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        low,high = 0, len(S)-1
        while low < high:
            if not(S[low].isalpha()):
                low += 1
                continue
            elif not(S[high].isalpha()):
                high -= 1
                continue
            S[low], S[high] = S[high], S[low]
            low += 1
            high -= 1
        return "".join(S)