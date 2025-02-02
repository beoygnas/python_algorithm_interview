import collections 
import sys
sys.setrecursionlimit(1000000)

N,M,K = [int(x) for x in input().split()]

candy = [0] + [int(x) for x in input().split()]
root = {(i+1):(i+1) for i in range(N)}

def find(x) :
    if root[x] != x :
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    root[find(x)] = find(y)
    
for _ in range(M) :
    x, y = [int(x) for x in input().split()]
    union(x, y)

friends, candies = collections.defaultdict(int), collections.defaultdict(int)

for k in root :
    friends[find(k)] += 1
    candies[find(k)] += candy[k]

arr = [(0,0)] + [(friends[i], candies[i]) for i in friends]
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
