"""
Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SolutionDvivideAndConquer:
    # Time Complexity: O(Nlogk)
    # Space Complexity: O(1)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
      if not lists: return None
      length = len(lists)
      interval = 1
      while interval < length:
        for i in range(0, length - interval, interval *2):
          lists[i] = self.mergeLists(lists[i], lists[i+interval])
        interval *= 2
      return lists[0]
      
    def mergeLists(self, l1, l2):
      if not l1 or not l2:
        return l1 or l2
      head = ListNode(0)
      cur = head
      while l1 and l2:
        if l1.val < l2.val:
          cur.next = l1
          l1 = l1.next
        else:
          cur.next = l2
          l2 = l2.next
        cur = cur.next
      if l1 or l2:
        cur.next = l1 or l2
      return head.next


from queue import PriorityQueue
class Solution_pq:
    # Time Complexity: O(Nlogk) - N is the total no of nodes and k is no of lists
    # Space Complexity: O(k)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
      head = cur = ListNode(0)
      q = PriorityQueue()
      # used to differentiate when two node values are equal else PriorityQueue raises error
      count = 0
      for l in lists:
        if l:
          q.put((l.val, count, l))
          count += 1
      
      while not q.empty():
        val, counter, node = q.get()
        cur.next = node
        cur = cur.next
        node = node.next
        if node:
          q.put((node.val, count+1, node))
          count += 1
      return head.next


class Solution:
    # NOT ACCEPTED
    """
    Time complexity : O(kN)O where k is the number of linked lists.
        Almost every selection of node in final linked costs O(k) (k-1 times comparison).
        There are N nodes in the final linked list.
    Space Complexity: O(1) It's not hard to apply in-place method - 
        connect selected nodes instead of creating new nodes to fill the new linked list.
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
      res = ListNode(0)
      cur = res
      while cur:
        # Compare every k nodes (head of every linked list) and get the node with the smallest value.
        minNode,index = None, -1
        for i in range(len(lists)):
          if lists[i]:
            if not minNode or minNode.val > lists[i].val:
              minNode = lists[i]
              index = i
        if index != -1:
          lists[index] = lists[index].next
        cur.next, cur = minNode, minNode
      return res.next