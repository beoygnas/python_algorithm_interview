# 주어진 두 정점을 반드시 지나가야함.
# (다익스트라 * 3) * 2

import collections
import heapq
import sys
input=sys.stdin.readline
graph = collections.defaultdict(list)

def dijkstra(start, end): 
    
    d = [float('inf')] * (N+1)
    pq = [(0, start)]
    d[start] = 0
    
    while pq :
        cost, cur = heapq.heappop(pq)
        if cost > d[cur] : 
            continue
        if cur == end :
            return cost
        for nxt, weight in graph[cur]: 
            if cost+weight < d[nxt] :
                heapq.heappush(pq, (cost+weight, nxt))
                d[nxt] = cost+weight
        
    return float('inf')

N, E = [int(x) for x in input().split()]
for _ in range(E):
    a, b, c = [int(x) for x in input().split()]
    graph[a].append((b,c))
    graph[b].append((a,c))
    
n, m = [int(x) for x in input().split()]

nm = dijkstra(1,n)+dijkstra(n,m)+dijkstra(m,N)
mn = dijkstra(1,m)+dijkstra(m,n)+dijkstra(n,N)

print(-1 if min(nm,mn) == float('inf') else min(nm,mn))
    
