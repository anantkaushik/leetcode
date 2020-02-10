"""
Problem Link: https://leetcode.com/problems/remove-linked-list-elements/

Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = dummy_head
        while cur.next:
          if cur.next.val == val:
            cur.next = cur.next.next
          else:
            cur = cur.next
        return dummy_head.next
