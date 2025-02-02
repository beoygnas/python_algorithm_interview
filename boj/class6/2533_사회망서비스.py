# 트리와 DP
# Leaf node 부터 쭉 올라간다.
# 서브트리에서 최소로 얼리어답터를 계속해서 사용하면 됨.
# 자기 자신이 얼리어답터이냐, 아니냐도 따진다.
# d[i][0, 1]: i의 서브트리에서 최소 얼리어답터 수

import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
graph = collections.defaultdict(list)
vis = collections.defaultdict(int)
d = [[0, 0] for _ in range(N+1)]

for _ in range(N-1):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)
    
def dfs(n):
    vis[n] = 1
    d[n][0] = 0
    d[n][1] = 1
    
    for nxt in graph[n] :
        if not vis[nxt] : 
            dfs(nxt)
            d[n][0] += d[nxt][1] # 얼리어답터아니면 무조건 상대는 얼리어답터
            d[n][1] += min(d[nxt]) # 자기 자신이 얼리어답터면 상관x

dfs(1)
print(min(d[1][0], d[1][1]))

