# https://leetcode.com/problems/reverse-linked-list-ii

from typing import * 
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 0. 내가 푼 풀이
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 구현만 조금 귀찮을 듯.
        # index부터 찾아야하나 left - 1 부터 찾자.
        
        left_adjacent_node, right_adjacent_node, left_node = None, None, None
        root = head
        idx = 1
        rev = None
        while head : 
            if idx == left - 1: 
                left_adjacent_node = head
            if idx == right + 1 :
                right_adjacent_node = head
            if idx >= left and idx <= right :
                if idx == left : 
                    left_node = head
                if idx == right : 
                    right_adjacent_node = head.next
                p, head = head, head.next
                idx += 1 
                rev, rev.next = p, rev
                
            else :
                head = head.next
                idx += 1
        
        left_node.next = right_adjacent_node
        if left_adjacent_node : 
            left_adjacent_node.next = rev
            return root 
        else : 
            return rev
        
# 1. 반복 구조로 노드 뒤집기
# 뒤에 있는 노드를 저장할 tmp만 필요.   
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or left == right : 
            return head

        root = start = ListNode()
        root.next = head
        
        for _ in range(left-1) :
            start = start.next # left adjacent (left - 1)
        end = start.next # left

        for _ in range(right - left) : 

            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
            # tmp, start.next, end.next = start.next, end.next, end.next.next
            # start.next.next = tmp
        return root.next