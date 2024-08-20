# https://leetcode.com/problems/network-delay-time
import heapq
from typing import * 
import collections

# 0. 힙에다가, 간선 weight를 주는 방식. 
# memory limit excceeded 문제 발생 + 간선 weight로 그리디하게 할 수 없어서 조건이 붙음 (Line 23)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # k번 노드에서 1~n번 노드까지 최단거리 찾기

        answer = [-1] * (n+1)
        heap = []
        graph = collections.defaultdict(list)
        
        for u, v, w in times : 
            graph[u].append((v, w))
            
        heapq.heappush(heap, (0, k, 0))
    
        while heap : 
            edge, node, prev = heapq.heappop(heap)
        
            if answer[node] != -1 and answer[node] < prev + edge : continue
            answer[node] = prev + edge
            
            for nxt_node, weight in graph[node] :
                heapq.heappush(heap, (weight, nxt_node, answer[node]))
            
        if -1 in answer[1:] :
            return -1
        else :
            return max(answer[1:])

# 1. 힙에다가 edge를 더한 값을 그냥 넣어주는 방식, 불필요한 condition이 필요없음.
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        answer = [-1] * (n+1)
        heap = []
        graph = collections.defaultdict(list)
        
        for u, v, w in times : 
            graph[u].append((v, w))
            
        heapq.heappush(heap, (0, k))
    
        while heap : 
            distance, node = heapq.heappop(heap)
        
            if answer[node] != -1 : continue
            answer[node] = distance
            
            for nxt_node, weight in graph[node] :
                heapq.heappush(heap, (distance + weight, nxt_node))
            
        if -1 in answer[1:] :
            return -1
        else :
            return max(answer[1:])
        
# 2. defaultdict를 적극 활용
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        answer, graph = collections.defaultdict(int), collections.defaultdict(list)
        
        for u, v, w in times : 
            graph[u].append((v, w))
            
        heapq.heappush(heap, (0, k))
    
        while heap : 
            distance, node = heapq.heappop(heap)
        
            if node in answer : continue
            answer[node] = distance
            
            for nxt_node, weight in graph[node] :
                heapq.heappush(heap, (distance + weight, nxt_node))
            
        if len(answer) == n :
            return max(answer.values())
        else :
            return -1