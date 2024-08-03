# https://leetcode.com/problems/add-two-numbers

from typing import * 
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 0. 내가 푼 풀이 : 접근방식은 비슷하나, 따로 ans의 메모리나, 순회할때마다 노드 생성하지 않고, l1으로 몰아주기
# l1의 길이가 짧을 때의 코드를 추가로 해줌.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # ans에 다 저장해두고 마지막에 reverse -> 시간복잡도는 O(n)이지만 reverse 구현까지해서 좀 귀찮
        # l1, l2의 길이만 알면, 하나에 더해가면서 하면 될텐데. 길이 하는 것도 귀찮.
        root = l1
        carry = 0

        while l1 or l2 : 
            l1.val += carry
            if l2  : l1.val += l2.val
            if l1.val >= 10 : 
                l1.val -= 10
                carry = 1
            else : 
                carry = 0
    
            if l1 and l2 and l1.next is None : 
                l1.next, l2.next = l2.next, l1.next

            if l1 : 
                if l1.next is None and carry == 1: 
                    l1.next = ListNode()
                l1 = l1.next
            if l2 : l2 = l2.next
            
        return root

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ans = ListNode(0)
        carry = 0

        while l1 or l2 or carry: 
            sum = carry
            if l1 : sum += l1.val
            if l2 : sum += l2.val
            
            if sum >= 10 : 
                sum -= 10
                carry = 1
            else : 
                carry = 0
        
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next

            ans.next = ListNode(sum)
            ans = ans.next

        return root.next

