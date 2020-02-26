"""
Problem Link: https://leetcode.com/problems/closest-divisors/

Given an integer num, find the closest two integers in absolute difference whose product equals 
num + 1 or num + 2.

Return the two integers in any order. 

Example 1:
Input: num = 8
Output: [3,3]

Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, 
the closest divisors are 2 & 5, hence 3 & 3 is chosen.

Example 2:
Input: num = 123
Output: [5,25]

Example 3:
Input: num = 999
Output: [40,25]
 
Constraints:
1 <= num <= 10^9
"""
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for x in range(int((num+2)**0.5), 0 , -1):
          if (num+1) % x == 0:
            return [x, (num+1)//x]
          elif (num+2) % x == 0:
            return [x, (num+2)//x]

"""
The reason for doing it from sqrt is that the factors start repeating in the reverse 
order after the square root.
eg: 100

The table produced is:
1*100    ^
2*50     |
4*25     |
5*20     |  (Increasing distance as we go up)
10*10 <- sqrt, we see repetitions after this point (Also notice this is the closest)
20*5 
25*4 
2*50 
100*1
"""