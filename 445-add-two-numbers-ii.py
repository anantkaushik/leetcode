"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes 
first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1,len2 = self.getLength(l1),self.getLength(l2)
        if len1 > len2:
            l2 = self.addLeadingZeroes(len1-len2,l2)
        else:
            l1 = self.addLeadingZeroes(len2-len1,l1)
        carry, summ = self.addNumbers(l1,l2)
        if carry > 0:
            new = ListNode(carry)
            new.next = summ
            summ = new
        return summ
        
    def getLength(self, node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count
    
    def addLeadingZeroes(self,count,node):
        for i in range(count):
            new = ListNode(0)
            new.next = node
            node = new
        return node
    
    def addNumbers(self,l1,l2):
        if not l1 and not l2:
            return (0,None)
        carry,new = self.addNumbers(l1.next,l2.next)
        summ = l1.val + l2.val + carry
        ans = ListNode(summ%10)
        ans.next = new
        return (summ//10,ans)