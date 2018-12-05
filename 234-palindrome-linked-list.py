"""
Problem Link: https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n = self.length(head)
        if n <= 1:
            return True
        firstHalfRev, secondHalf = self.rev(head,int(n/2))
        if n % 2 != 0:
            secondHalf = secondHalf.next
        while secondHalf:
            if secondHalf.val != firstHalfRev.val:
                return False
            secondHalf = secondHalf.next
            firstHalfRev = firstHalfRev.next
        return True
    
    def rev(self, node, l):
        newHead = None
        for i in range(l):
            if newHead is None:
                newHead = node
                node = node.next
                newHead.next = None
            else:
                tmp = node
                node = node.next
                tmp.next = newHead
                newHead = tmp
        return newHead,node
        
    def length(self, head):
        count = 0
        while (head):
            count = count + 1
            head = head.next
        return count