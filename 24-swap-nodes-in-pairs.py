"""
Problem Link: https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head:
        #     return None
        # cur = head.next if head.next else head
        # prev = None
        # while head and head.next:
        #     temp = head.next
        #     head.next = head.next.next
        #     temp.next = head
        #     head = head.next
        #     if prev:
        #         prev.next = temp
        #     prev = temp.next
        # return cur
        if head is None or head.next is None:
            return head
        nextHead = head.next.next
        newHead = head.next
        head.next.next = head
        head.next = self.swapPairs(nextHead)
        return newHead