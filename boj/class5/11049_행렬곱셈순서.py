# 이것역시 DP
import sys
N = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

d = [[0] * N for _ in range(N)]

for i in range(N-1): 
    d[i][i+1] = matrix[i][0] * matrix[i][1] * matrix[i+1][1]

for idx in range(2, N):
    i = (N-1)-idx 
    for j in range(i+2, N):
        d[i][j] = float('inf')
        for k in range(i, j):
            d[i][j] = min(d[i][j], d[i][k]+d[k+1][j]+matrix[i][0]*matrix[k][1]*matrix[j][1])
            
print(d[0][N-1])