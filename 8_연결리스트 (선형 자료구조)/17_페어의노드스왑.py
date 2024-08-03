# https://leetcode.com/problems/swap-nodes-in-pairs

from typing import * 
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 0. 내가 푼 풀이 :재귀
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 두 칸씩 순회하면서 swap을 구현 -> 앞에껄 고려못함.
        # 앞뒤로 고려해줘야 함.
        # 재귀? swap 하고 이어주고, 스왑하고, 이어주고
        if head is None : return None
        if head.next is None : return head
        
        first_node, second_node = head, head.next

        if second_node.next is None : 
            first_node.next = None
            second_node.next = first_node
            return second_node
        else : 
            first_node.next = self.swapPairs(second_node.next)
            second_node.next = first_node
            return second_node
        
# 1. 같은 방법, 코드 깎기
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 위에서 불필요한 반복문을 제거할 수 있었음.
        if head and head.next : 
            first_node, second_node = head, head.next
            first_node.next = self.swapPairs(second_node.next)
            second_node.next = first_node
            return second_node
        return head
    
# 2. 더 깎기
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # firstNode라는 변수를 삭제할 수도, 하지만 가독성이 좋은지는 모르겠음.
        if head and head.next : 
            second_node = head.next
            head.next = self.swapPairs(second_node.next) # 사실상 firstNode.next
            second_node.next = head 
            return second_node
        return head
    
# 3. iteration, 처음에 이 방식을 생각했는데, prev라는 추가 메모리를 둬서 ans list를 만들 생각을 못했음.
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode()
        prev.next = head

        while head and head.next :
            second = head.next
            head.next = second.next
            second.next = head

            prev.next = second

            head = head.next
            prev = prev.next.next
        return root.next