# https://leetcode.com/problems/reverse-linked-list/

from typing import * 
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# 0. 내가 푼 풀이 : 실패
# 뒤에거를 reveerse 하고, 그 뒤에 현재 노드 붙이기. 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next : 
            # 연결리스트의 마지막 element에 추가는 O(n) 이라 실패 -> 구현 안함.
            self.reverseList(head.next).next = ListNode(head.val, None)
        return head
    
# 1. 재귀방식 풀이
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(self, node:ListNode, prev: ListNode=None) :
            if not node : 
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
            
        return reverse(head)
    
# 2. iteration
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        while head :
            rev, rev.next, head = head, rev, head.next
        
        return rev
        
# 2와 같은 방식이지만, 가독성을 위해 변수 하나 추가₩    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        while head :
            next, head.next = head.next, rev
            rev, head = head, next
        return rev