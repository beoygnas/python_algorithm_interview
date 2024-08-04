# https://leetcode.com/problems/design-circular-queue
import collections
from typing import * 

# 1. list를 이용
# empty와 full의 조건이 같기 때문에 추가적인 조건이 더 필요함.
# -> list가 None일 경우로 대체
class MyCircularQueue:

    def __init__(self, k: int):
        self.length = k
        self.q = [None] * k
        self.front = 0 
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull() : return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.length
        return True

    def deQueue(self) -> bool:
        if self.isEmpty() : return False
        self.q[self.front] = None
        self.front = (self.front + 1) % self.length
        return True

    def Front(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None  

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None