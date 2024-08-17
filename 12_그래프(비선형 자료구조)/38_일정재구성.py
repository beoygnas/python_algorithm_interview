# https://leetcode.com/problems/reconstruct-itinerary
from typing import * 
import itertools
import collections

# 1. dfs + 재귀 어렵다
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    
        ticket_dict = collections.defaultdict(list)
        for dep, dst in sorted(tickets, reverse = True) : 
            ticket_dict[dep].append(dst)
        
        answer = []
        
        def dfs(dep) :
            while ticket_dict[dep] : 
                dfs(ticket_dict[dep].pop())
            answer.append(dep)

        dfs("JFK")
    
        return answer[::-1]
    
# 2. 재귀 말고 반복으로 풀기
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    
        ticket_dict = collections.defaultdict(list)
        for dep, dst in sorted(tickets, reverse = True) : 
            ticket_dict[dep].append(dst)
        
        answer, stack = [], ["JFK"]
        
        while stack : 
            while ticket_dict[stack[-1]] : 
                stack.append(ticket_dict[stack[-1]].pop())
            answer.append(stack.pop())
    
        return answer[::-1]