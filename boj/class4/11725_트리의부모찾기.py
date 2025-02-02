# bfs
import collections
import sys
input = sys.stdin.readline
n = int(input())
graph = collections.defaultdict(list)
vis = collections.defaultdict(int)

for _ in range(n-1):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)
    
q = collections.deque([1])
vis[1] = 1

while q: 
    cur = q.popleft()
    for nxt in graph[cur]: 
        if not vis[nxt] : 
            vis[nxt] = cur
            q.append(nxt)

for i in range(2, n+1) :
    print(vis[i])
