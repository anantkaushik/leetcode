"""
Problem Link: https://leetcode.com/problems/design-linked-list/

Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. 
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and 
next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more 
attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:
get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, 
                the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the 
                        length of linked list, the node will be appended to the end of linked list. If index is greater 
                        than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

Example:
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3

Note:
All values will be in the range of [1, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in LinkedList library.
"""
class Node:
    def __init__(self, data = None):
        self.val = data
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.length or index < 0:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        temp = Node(val)
        if not self.head:
            self.head = temp
            self.tail = self.head
        else:
            temp.next = self.head
            self.head = temp
        self.length += 1
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        temp = Node(val)
        if not self.tail:
            self.tail = temp
            self.head = self.tail
        else:
            self.tail.next = temp
            self.tail = temp
        self.length += 1
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > self.length or index < 0:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            temp = Node(val)
            cur = self.head
            for _ in range(index-1):
                cur = cur.next
            temp.next = cur.next
            cur.next = temp
            self.length += 1
        
    def deleteHead(self):
        if not self.head:
            return
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        
    def deleteTail(self):
        if not self.tail:
            return
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            cur = self.head
            while cur.next != self.tail:
                cur = cur.next
            cur.next = None
            self.tail = cur
        self.length -= 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index >= self.length:
            return
        if index == 0:
            self.deleteHead()
        elif index == self.length - 1:
            self.deleteTail()
        else:
            cur = self.head
            for _ in range(index-1):
                cur = cur.next
            cur.next = cur.next.next
            self.length -= 1