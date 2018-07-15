"""
 A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

"""
class Solution:
    def selfDividingNumbers(self, left, right):
        numbers = []
        for i in range(left,right+1):
            if i < 10:
                numbers.append(i)
            else:
                temp = i
                flag = 0
                while temp > 0:
                    n = temp % 10
                    if n == 0:
                        flag = 1
                        break
                    else:
                        if i % n != 0:
                            flag = 1
                            break
                    temp = temp // 10
                if flag == 0:
                    numbers.append(i)
        return numbers
