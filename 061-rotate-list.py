"""
Problem Link: https://leetcode.com/problems/rotate-list/

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL

Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL

Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        l = self.length(head)
        k = k % l
        if l == 1 or k % l == 0:
            return head
        count = 0
        curr = head
        while count < l-k:
            prev = head
            head = head.next
            count += 1
        prev.next = None
        result = head
        while head.next:
            head = head.next
        head.next = curr
        return result
        
    def length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count