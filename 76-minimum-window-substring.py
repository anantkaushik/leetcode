"""
Problem Link: https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".
Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"
 
Constraints:
1 <= s.length, t.length <= 105
s and t consist of English letters.

Follow up: Could you find an algorithm that runs in O(n) time?
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        
        # counter represents the number of chars of t to be found in s.
        start, end, min_len, min_start, counter = 0, 0, float('inf'), 0, len(t)
        
        while end < len(s):
            
            # If char in s exists in t, decrease counter
            if count.get(s[end], 0) > 0:
                counter -= 1
            
            # Decrease count[s[end]]. If char does not exist in t, count[s[end]] will be negative.
            count[s[end]] = count.get(s[end], 0) - 1
            
            end += 1
            
            # When we found a valid window, move start to find smaller window.
            while counter == 0:
                
                if (end - start) < min_len:
                    min_len = end - start
                    min_start = start
                
                count[s[start]] += 1
                
                # When char exists in t, increase counter.
                if count[s[start]] > 0:
                    counter += 1
                
                start += 1
        
        return s[min_start: min_start + min_len] if min_len != float('inf') else ""
