"""
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true

Example 2:
Input: 16
Output: true

Example 3:
Input: 218
Output: false
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and not(n & n-1)

"""
Explanation:
At a power of 2, we only have one bit set to 1 at its respective decimal place (e.g. 1000).
At the power of 2 minus 1, we have all the bits before the current decimal place set to 1 (e.g. 0111), which means that n & (n - 1) == 0 
for powers of 2.
The reason why this happens is because we're in the binary number system and a power of 2 means we're going to the next decimal place 
(i.e. 0111 + 1 = 1000).

What about when n is not a power of 2? If you look at a list of binary numbers:
0100
0101
0110
0111
1000

Remember how the power of 2 is the special case where adding 1 results in us moving to the next decimal place (i.e. 0111 + 1 = 1000)? 
Since every other case doesn't result in that, there is at least the current power of 2's 1 bit overlapping with whatever the number 
is (i.e. we're at 0100, 0101 will always share the 0100 bit. The only time the 0100 bit becomes 0 again is if we go to the next power of 2).
"""