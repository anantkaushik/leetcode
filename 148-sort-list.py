"""
Problem Link: https://leetcode.com/problems/sort-list/

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        middleNode = self.findMiddleNode(head)
        right = middleNode.next
        middleNode.next = None
        return self.mergeList(self.sortList(head), self.sortList(right))
        
    def findMiddleNode(self, head):
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def mergeList(self,left,right):
        dummy = ListNode(None)
        node = dummy
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
            
        node.next = left or right
        return dummy.next