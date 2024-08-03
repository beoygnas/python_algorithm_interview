# https://leetcode.com/problems/odd-even-linked-list

from typing import * 
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 0. 내가 푼 풀이
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 짝/홀 runner를 시켜서 각각 연결, 이후에 이어주기.
        
        odd = odd_head = ListNode()
        even = even_head = ListNode()

        while head and head.next : 
            odd.next, even.next = head, head.next
            odd, even = odd.next, even.next            
            head = head.next.next
        
        odd.next, even.next = head, None
    
        if odd.next is not None : odd = odd.next
        odd.next = even_head.next
        
        return odd_head.next

# 1. 같은 방식이지만 공간복잡도 줄이기
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        if head is None : return None

        odd = head
        even = even_head = head.next

        while even and even.next : 
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        odd.next = even_head
        
        return head