"""
Problem Link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, 
which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, 
and so on, to produce a multilevel data structure, as shown in the example below.
Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of 
the first level of the list.

Example 1:
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Example 2:
Input: head = [1,2,null,3]
Output: [1,3,2]

Explanation:

The input multilevel linked list is as follows:
  1---2---NULL
  |
  3---NULL

Example 3:
Input: head = []
Output: []
 
How multilevel linked list is represented in test case:
We use the multilevel linked list from Example 1 above:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

The serialization of each level is as follows:
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

To serialize all levels together we will add nulls in each level to signify no node connects to the upper 
node of the previous level. The serialization becomes:
[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 
Constraints:
Number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self,node: 'Node', next_node=None) -> 'Node':
        if not node:
            return
                
        if not node.child and not node.next and next_node:
            node.next = next_node
            node.next.prev = node
            return node
                
        node.next = self.flatten(node.next, next_node)
        if node.child:
            node.next = self.flatten(node.child, node.next)
            node.child = None
            node.next.prev = node
                  
        return node


class Solution1:
    def flatten(self,node: 'Node', next_node=[]) -> 'Node':
        if not node:
            return
        
        
        if not node.child and not node.next and next_node:
            node.next = self.flatten(next_node.pop())
            if node.next:
                node.next.prev = node
            
        elif node.child:
            next_node.append(node.next)
            node.next = self.flatten(node.child, next_node)
            node.child = None
            node.next.prev = node
        else:
            self.flatten(node.next, next_node)
        return node


class Solution2:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        
        cur = head
        
        while cur:
            if cur.child:
                temp = cur.next
                cur.next = cur.child
                cur.child = None
                cur.next.prev = cur
                child_head = cur.next
                
                while child_head.next:
                    child_head = child_head.next
                child_head.next = temp
                if temp:
                    temp.prev = child_head
                    
            cur = cur.next
        
        return head
