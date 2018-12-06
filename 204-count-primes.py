"""
Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        prime = [1]*(n)
        prime[0] = prime[1] = 0
        for i in range(2, int(n**0.5)+1):
            if prime[i] == 1:
                prime[i*i:n:i] = [0] * int((n-i*i-1)/i + 1)
                """
                if prime[i] == 1:
                for j in xrange(i*i,n,i):
                    prime[j] = 0 
                """
        return sum(prime) 