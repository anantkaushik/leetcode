"""
Problem Link: https://leetcode.com/problems/fizz-buzz/

Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output 
“Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
class Solution:
    def fizzBuzz(self, n):
        result = []
        r5 = "Buzz"
        r3 = "Fizz"
        for i in range(1,n+1):
            print(i)
            if i % 3 == 0 and i % 5 ==0:
                result.append(r3+r5)
            elif i % 3 == 0:
                result.append(r3)
            elif i % 5 == 0:
                result.append(r5)
            else:
                result.append(str(i))
        return result
