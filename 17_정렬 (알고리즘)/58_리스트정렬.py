# https://leetcode.com/problems/sort-list

from typing import * 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 0. 내장함수와, 연결리스트를 array로 정렬        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        while head : 
            li.append(head.val)
            head = head.next
        li.sort()

        root = ListNode()
        node = root

        for x in li :
            node.next = ListNode(x)
            node = node.next
        
        return root.next

# 1. linked list를 분할정복하여 정렬하는 merge sort
# 절반을 자르는 것을, runner를 통해서 구현

class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
        if l1 and l2 : 
            if l1.val > l2.val :
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)        
        return l1 or l2


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next) : 
            return head
        
        half, slow, fast = None, head, head
        while fast and fast.next : 
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head) # 절반
        l2 = self.sortList(slow) # 나머지 뒤에 절반

        return self.mergeTwoLists(l1, l2)



