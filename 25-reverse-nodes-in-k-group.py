"""
Problem Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
      if k == 1 or not head:
        return head
      count = 0
      dummyHead = ListNode(0)
      dummyHead.next = head
      begin = dummyHead
      while head:
        count += 1
        # If (head - begin) == k
        if count % k == 0:
          begin = self.reverseList(begin, head.next)
          head = begin.next
        else:
          head = head.next
      return dummyHead.next
    
    def reverseList(self, begin, end):
      cur = begin.next
      prev = begin
      first = cur
      while cur != end:
        cur.next, prev, cur = prev, cur, cur.next
      begin.next = prev
      first.next = cur
      return first

class SolutionRecursive:
    # Time Complexity: O(n)
    # Space Complexity: O(n/k)
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        newhead = head
        for i in range(k):
            if newhead == None:
                return head
            newhead = newhead.next
        connect = cur= head
        prev = None
        for i in range(k):
            cur.next, cur, prev = prev, cur.next, cur
        connect.next = self.reverseKGroup(newhead,k)
        return prev