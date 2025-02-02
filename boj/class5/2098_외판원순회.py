# 비트마스킹 + DP
# 시간복잡도 2^16 * 16 * 16 = 2^24 = 1677,0000
import sys
input = sys.stdin.readline

N = int(input())
W = [[int(x) for x in input().split()] for _ in range(N)]

# d[16][2^16] : i~j까지, 다녀온데를 고려한 최소 거리
# answer d[n][2^16-1]
d = [[-1] * (1<<N) for _ in range(N)]

def dfs(node, visited):
    if visited == (1<<N)-1:
        return float('inf') if W[node][0] == 0 else W[node][0]
    
    if d[node][visited] != -1:
        return d[node][visited]

    for nxt in range(1, N):
        if W[node][nxt] != 0 and visited & (1<<nxt) == 0:
            if d[node][visited] == -1 :
                d[node][visited] = dfs(nxt, visited|(1<<nxt)) + W[node][nxt]
            else : 
                d[node][visited] = min(d[node][visited], dfs(nxt, visited|(1<<nxt)) + W[node][nxt])

    if d[node][visited] == -1:
        return float('inf')
    
    return d[node][visited]

print(dfs(0,1))