import collections
from typing import *

# open addressing 방법 
# 배열의 크기를 늘려서 collision을 무시
class MyHashMap:

    def __init__(self):
        self.map = [None] * 1000005
        
    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if self.map[key] is None :
            return -1
        return self.map[key]
        
    def remove(self, key: int) -> None:
        self.map[key] = None


# 1. Chaining을 통한 구현
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [ListNode()] * self.size
        
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        
        if self.table[index].value is None :
            self.table[index] = ListNode(key, value)
        else : 
            cur = self.table[index]
            while cur :
                if key == cur.key : 
                    cur.value = value
                    return
                if cur.next is None : 
                    break
                cur =  cur.next
            cur.next = ListNode(key, value)
            
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None :
            return -1
        
        cur = self.table[index]
        while cur : 
            if key == cur.key :
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None :
            return 
        
        cur = self.table[index]
        if key == cur.key : 
            self.table[index] = ListNode() if cur.next is None else cur.next
            return
        
        prev = cur
        while cur : 
            if key == cur.key :
                prev.next = cur.next
                return
            prev, cur = cur, cur.next