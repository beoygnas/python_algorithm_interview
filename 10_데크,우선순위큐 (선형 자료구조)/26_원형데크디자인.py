#  https://leetcode.com/problems/design-circular-deque

import collections
from typing import * 

# 0. 원형큐디자인에서 insertfront, deleteLast 만 추가
class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [None] * k
        self.front = 0
        self.rear = 0
        self.length = k

    def insertFront(self, value: int) -> bool:
        if self.isFull() : return False
        self.front = (self.length - 1) if self.front == 0 else self.front - 1
        self.q[self.front] = value
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull() : return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.length
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty() : return False
        self.q[self.front] = None
        self.front = (self.front + 1) % self.length
        return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty() : return False
        self.rear = (self.length - 1) if self.rear == 0 else self.rear - 1
        self.q[self.rear] = None 
        return True

    def getFront(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]

    def getRear(self) -> int:
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None



## 링크드 리스트로 구현
class ListNode : 
    def __init__(self, item=0, left=None, right=None) : 
        self.item = item
        self.left = left
        self.right = right

class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.max_len, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
        self.head.left, self.tail.right = self.tail, self.head

    def _add(self, node: ListNode, new_node: ListNode) : 
        right_node = node.right
        node.right = new_node
        new_node.left, new_node.right = node, right_node
        right_node.left = new_node

    def _del(self, node: ListNode) : 
        n = node.right.right
        node.right, n.left = n, node

    def insertFront(self, value: int) -> bool:
        if self.isFull() : return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull() : return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty() : return False
        self.len -= 1
        self._del(self.head)

        return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty() : return False
        self.len -= 1
        self._del(self.tail.left.left)

        return True

    def getFront(self) -> int:
        return -1 if self.head.right.item is None else self.head.right.item

    def getRear(self) -> int:
        return -1 if self.tail.left.item is None else self.tail.left.item

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.max_len