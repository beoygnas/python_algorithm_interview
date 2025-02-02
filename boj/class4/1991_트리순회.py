import collections
import sys
sys.setrecursionlimit(10**7)
graph = collections.defaultdict(list)
vis = collections.defaultdict(int)

N = int(input())
pre_order, in_order, post_order = '', '', ''

for _ in range(N) : 
    p, l, r = input().split()
    graph[p] = [l, r]

def dfs(node) :
    global in_order, pre_order, post_order
    
    vis[node] = 1
    l, r = graph[node]
    pre_order += node
    if l != '.' and not vis[l] : 
        dfs(l)
    in_order += node
    if r != '.' and not vis[r] : 
        dfs(r)
    post_order += node

dfs('A')
print(pre_order)
print(in_order)
print(post_order)