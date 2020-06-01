"""
Problem Link: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

Given a binary string s and an integer k.
Return True if all binary codes of length k is a substring of s. Otherwise, return False.

Example 1:
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". 
They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.

Example 2:
Input: s = "00110", k = 2
Output: true

Example 3:
Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 

Example 4:
Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and doesn't exist in the array.

Example 5:
Input: s = "0000000001011100", k = 4
Output: false
 
Constraints:
1 <= s.length <= 5 * 10^5
s consists of 0's and 1's only.
1 <= k <= 20
"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # generate all combinations and store then in the set
        return len({s[i - k : i] for i in range(k, len(s) + 1)}) == 2 ** k


class Solution1:
    def hasAllCodes(self, s: str, k: int) -> bool:
      if len(s) < k:
        return False
      binary_numbers = set()
      for i in range(2**k):
        binary_numbers.add(bin(i)[2:].zfill(k))
      
      temp = s[:k]
      if temp in binary_numbers:
        binary_numbers.remove(temp)

      for i in range(k, len(s)):
        temp = temp[1:] + s[i]
        if temp in binary_numbers:
          binary_numbers.remove(temp)
        
        if not binary_numbers:
          return True
      
      return False