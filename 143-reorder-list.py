"""
Problem Link: https://leetcode.com/problems/reorder-list/

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
          return 
        # Find the middle node
        slow = fast = head
        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
        
        # reverse the second half
        prev = None
        while slow:
          temp = slow
          slow = slow.next
          temp.next = prev
          prev = temp
        
        start = head
        while prev.next:
          start.next, start = prev, start.next
          prev.next, prev = start, prev.next
          
          