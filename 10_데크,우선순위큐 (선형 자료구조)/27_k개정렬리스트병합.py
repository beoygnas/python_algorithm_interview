# https://leetcode.com/problems/merge-k-sorted-lists

import collections
import heapq
from typing import * 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        root = runner = ListNode(None)
        heap = [] #queue

        for i in range(len(lists)) : 
            if lists[i] :
                heapq.heappush(heap, (lists[i].val, i, lists[i])) 
                # queue에 heap push
                # item = (value, index, node) == (lists[i].val, i, list[i])

        while heap : 
            node = heapq.heappop(heap) # 가장 작은거 get
            idx = node[1] 
            runner.next = node[2]
            
            runner = runner.next   
            
            if runner.next : 
                heapq.heappush(heap, (runner.next.val, idx, runner.next))
        
        return root.next