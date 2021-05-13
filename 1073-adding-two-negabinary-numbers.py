"""
Problem Link: https://leetcode.com/problems/adding-two-negabinary-numbers/

Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit. 
For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  
A number arr in array, format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.
Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

Example 1:
Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
Output: [1,0,0,0,0]
Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.

Example 2:
Input: arr1 = [0], arr2 = [0]
Output: [0]

Example 3:
Input: arr1 = [0], arr2 = [1]
Output: [1]

Constraints:
1 <= arr1.length, arr2.length <= 1000
arr1[i] and arr2[i] are 0 or 1
arr1 and arr2 have no leading zeros
"""
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        carry = 0
        arr1_index = len(arr1) - 1
        arr2_index = len(arr2) - 1
        
        res = []
        while arr1_index >= 0 or arr2_index >= 0 or carry:
            # print(carry, res)
            arr1_value = arr1[arr1_index] if arr1_index >= 0 else 0
            arr2_value = arr2[arr2_index] if arr2_index >= 0 else 0
            
            cur_sum =  arr1_value + arr2_value + carry
            # print(cur_sum)
            
            res.append(cur_sum % 2)
            carry = -(cur_sum // 2)
            
            arr1_index -= 1
            arr2_index -= 1
        
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]
