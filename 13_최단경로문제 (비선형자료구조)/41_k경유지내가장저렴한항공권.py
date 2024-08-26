# https://leetcode.com/problems/cheapest-flights-within-k-stops

import heapq 
import collections


# 0. 다익스트라는 기본적으로 그리디여서 한번 방문하면 최소 거리가 되지만, 이 문제에서는 최소 가격이므로 그리디로 풀면안됨.
# 재방문이 가능하다는 것을 인지.
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        heap, graph, answer = [(0, src, 0)], collections.defaultdict(list), collections.defaultdict(int)
        for u,v,w in flights : 
            graph[u].append((v,w))

        while heap : 
            price, node, stops = heapq.heappop(heap)

            if node == dst : 
                return price
            if (answer[node] != 0 and answer[node] < stops) or stops > k : 
                continue

            answer[node] = stops
            for nxt_node, weight in graph[node] : 
                heapq.heappush(heap, (price+weight, nxt_node, stops + 1))

        
        return -1
    
    
# 1. 
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # greedy로 할 수 있나? -> 재방문을 고려할 수 있도록 수정이 필요함
        # pq에 넣을 때, k를 고려한다.
    
        graph, vis = collections.defaultdict(list), collections.defaultdict(int)
        for u,v,w in flights : 
            graph[u].append((v, w))
        
        pq = [(0, src, 0)]

        while pq : 
            total_price, node, stop = heapq.heappop(pq)

            if node == dst : 
                return total_price
            if stop <= k and (vis[node] == 0 or vis[node] > stop):
                vis[node] = stop
                for nxt, price in graph[node] :
                    heapq.heappush(pq, (total_price+price, nxt, stop + 1))
        
        return -1
