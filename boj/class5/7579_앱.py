import collections 
import sys
input = sys.stdin.readline

N,M,K = [int(x) for x in input().split()]

candies = [0] + [int(x) for x in input().split()]
    
graph, vis = collections.defaultdict(list), collections.defaultdict(int)

for _ in range(M) :
    x, y = [int(x) for x in input().split()]
    graph[x].append(y)
    graph[y].append(x)

def dfs(u):
    friends, candy= 0, 0
    stack = [u]
    vis[u] = 1
    while stack : 
        cur = stack.pop()
        friends += 1
        candy += candies[cur]
        for v in graph[cur] :
            if not vis[v] :
                vis[v] = 1
                stack.append(v)  
                
    return (friends, candy)         
           
arr = [(0,0)]
for u in range(1, N+1) : 
    if vis[u] : 
        continue
    arr.append(dfs(u))

n = len(arr)
d = [[0] * n for _ in range(K)]

answer = 0
for i in range(1, K):
    for j in range(1, n):
        d[i][j] = max(d[i][j-1], d[i-1][j])
        if arr[j][0] <= i :
            d[i][j] = max(d[i][j], d[i-arr[j][0]][j-1] + arr[j][1])
        answer = max(answer, d[i][j])

print(answer)