# https://leetcode.com/problems/insertion-sort-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 0. linked list에서 하나씩 뽑아 삽입정렬하기
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        root = ListNode(-inf)

        while head : 
            node = root
            
            while node.next and head.val > node.next.val :
                node = node.next

            new_node = ListNode(head.val)
            new_node.next = node.next
            node.next = new_node
            head = head.next

        return root.next

# 1. 하나씩 뽑을 때마다, 새로운 List를 만들지 않고 그냥 진행.
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = parent = ListNode(None)

        while head : 
            while cur.next and head.val > cur.next.val :
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next
            cur = parent

        return cur.next

# 2. 불필요한 비교연산을 줄이기 위해, 조건문 추가

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = parent = ListNode(-inf)

        while head : 
            while cur.next and head.val > cur.next.val :
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next
            
            if head and cur.val > head.val : # kick
                cur = parent

        return parent.next

