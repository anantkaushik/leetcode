"""
Problem Link: https://leetcode.com/problems/reverse-linked-list/description/

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
    """ 
    -------- Recursive Solution --------
    def reverseList(self, head, prev = None):
        if not head:
            return prev
        cur, head.next = head.next, prev
        return self.reverseList(cur,head)
    """