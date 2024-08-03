# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import * 
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 0. 연결리스트로 풀기 -> 실패
# 연결리스트의 head를 유지 못해서 실패함
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = None
        while list1 and list2 : 
            if list1.val > list2.val : 
                if not answer : answer = ListNode(list1.val, None)
                else : 
                    answer.next = ListNode(list1.val, None)
                    answer = answer.next
                list1 = list1.next
            else : 
                if not answer : answer = ListNode(list2.val, None)
                else : 
                    answer.next = ListNode(list2.val, None)
                    answer = answer.next
                list2 = list2.next

        return answer 

# 1. 재귀로 풀기
# 너무 간단...
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1) or (l2 and l1.val > l2.val) : 
            l1, l2 = l2, l1
        if l1 : 
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1