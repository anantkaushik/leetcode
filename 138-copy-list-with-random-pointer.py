"""
Problem Link: https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list is given such that each node contains an additional random pointer which could 
point to any node in the list or null.
Return a deep copy of the list.
The Linked List is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, 
or null if it does not point to any node.
 
Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Example 4:
Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.

Constraints:
-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    # Time Complexity - O(N)
    # Space Complexity - O(N)
    def copyRandomList(self, head: 'Node') -> 'Node':
        clone_map = {}
        cur = head
        # Give all nodes their clone in the mapping
        while cur:
          clone_map[cur] = Node(cur.val)
          cur = cur.next
          
        # Reset the cur pointer to the head of the original list
        # Give all clones their next and random pointer assignments.
        # Our clone_map lets us reach an original node's clone in 
        cur = head
        while cur:
          clone_map.get(cur).next = clone_map.get(cur.next)
          clone_map.get(cur).random = clone_map.get(cur.random)
          cur = cur.next
        return clone_map.get(head)
          
class Solution1:
    # Time Complexity : O(N)
    # Space  Complexity: O(1)
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
          new_node = Node(cur.val)
          cur.next, new_node.next = new_node, cur.next
          cur  = new_node.next

        cur = head
        while cur:
          if cur.random:
            cur.next.random = cur.random.next
          cur = cur.next.next
        
        cur = head
        dummyHead = Node(0)
        newCur = dummyHead
        while cur:
          newCur.next = cur.next
          cur = cur.next.next
          newCur = newCur.next 
        return dummyHead.next
          