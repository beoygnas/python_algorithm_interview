# 1. brute force: 모든 노드에 대해서 DFS, 10000^2 시간 초과
# 2. DFS : 노드마다 자식노드를 모두 탐색해서 가장 거리가 먼 두 노드의거리를 answer로 초기화, 가장 큰 걸 return

import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
graph = collections.defaultdict(list)
vis = collections.defaultdict(int)

for _ in range(n-1):
    u, v, w = [int(x) for x in input().split()]
    graph[u].append((v,w))
    graph[v].append((u,w))
    
    
answer = 0

def dfs(node):
    global answer
        
    vis[node] = 1
    result = [0,0]
    
    for child, distance in graph[node]: 
        if not vis[child] : 
            result.append(dfs(child) + distance)
    
    result.sort(reverse=True)
    answer = max(answer, result[0]+result[1])
    
    return result[0]
    
dfs(1)
print(answer)
    