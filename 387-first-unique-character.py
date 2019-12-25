"""
Problem Link: https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return 
it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
# Time Complexity: O(n)
# Space Complexity: O(1). As max size of dictionary will never exceed 26
class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabets = {}
        for c in s:
          alphabets[c] = alphabets.get(c,0) + 1
        
        for i in range(len(s)):
          if alphabets.get(s[i]) == 1:
            return i
        return -1
        
# Better solution as we're not iterating over the string two time
class Solution1:
    def firstUniqChar(self, s: str) -> int:
        alphabets = {}
        for idx, ch in enumerate(s):
          if ch not in alphabets:
		    # In alphabets i'm storing of array size 2
			# first index will store the value of occurence of character
			# second index will store the value of index of that character
            alphabets[ch] = [0,idx]
		 # Updating the value of occurence of character
		 # if the alphabet is appearing second time or more then it is not our answer 
		 # so not updating its index value
          alphabets[ch][0] += 1
		  
        # In Python3 dictionary maintain the order of data in which we inserted it
        for key,value in alphabets.items():
          if value[0] == 1:
            return value[1]
        return -1