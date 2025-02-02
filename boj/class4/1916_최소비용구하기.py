# 다익스트라

import heapq, collections
import sys
input = sys.stdin.readline

N, M = int(input()), int(input())
graph = collections.defaultdict(list)
costs = [float('inf')] * (N+1)

for _ in range(M) : 
    u, v, w = [int(x) for x in input().split()]
    graph[u].append((v,w))

start, end = [int(x) for x in input().split()]

pq = [(start,0)]
costs[start] = 0

while pq : 
    cur, cost = heapq.heappop(pq)
    if cost > costs[cur] : 
        continue
    
    for v, w in graph[cur] : 
        if cost + w < costs[v] :
            heapq.heappush(pq, (v, cost+w))
            costs[v] = cost+w

print(costs[end])
