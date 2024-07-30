# https://leetcode.com/problems/palindrome-linked-list/

from typing import * 
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 0. 순회하여 리스트에 쌓고, reverse check
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        palindrome = [head.val]
        while head.next is not None : 
            head.val = head.next.val
            head.next = head.next.next
            palindrome.append(head.val)
        
        return palindrome==palindrome[::-1]

# 1. 최적화
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        palindrome = []
        while head is not None : 
            palindrome.append(head.val)
            head = head.next
        
        return palindrome==palindrome[::-1]
    
# 2. list의 pop(0), O(n) 처리
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        palindrome = []
        while head is not None : 
            palindrome.append(head.val)
            head = head.next
        
        while len(palindrome) > 1 : 
            if palindrome.pop(0) != palindrome.pop() :
                return False
        return True

# 3. deq 이용 최적화
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        palindrome = collections.deque
        while head is not None : 
            palindrome.append(head.val)
            head = head.next
        
        while len(palindrome) > 1 : 
            if palindrome.popleft() != palindrome.pop() :
                return False
        return True
    
# 4. runner를 이용한 풀이
# fast runner가 도착할때, slow runner는 반칸에 도착하는 것을 이용.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next : 
            # fast runner 부터 두칸씩 이동
            fast = fast.next.next
            # slow runner 한칸 이동, rev도 동시에 할당
            rev, rev.next, slow = slow, rev, slow.next
            
        if fast : 
            slow = slow.next

        while rev and slow.val != rev.val :
            slow, rev = slow.next, rev.next
        
        return not rev
    
        # while slow :
        #     if slow.val != rev.val : return False
        #     slow, rev = slow.next, rev.next
        # return True
