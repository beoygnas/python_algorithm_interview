import collections 
import sys
input = sys.stdin.readline

N = int(input())
board = [[-int(x) for x in input().split()] for _ in range(N)]
queue = collections.deque([(0, (0,1))])
d = collections.defaultdict(int)
d[(0,0,1)] = 1

for i in range(2,N):
    if board[0][i] == 0 :
        d[(0,0,i)] =  1
    else :
        break

for i in range(1,N):
    for j in range(2,N):
        if board[i][j] == 0 :
            d[(0,i,j)] = d[(0,i,j-1)] + d[(1,i,j-1)] 
            d[(2,i,j)] = d[(2,i-1,j)] + d[(1,i-1,j)] 
            if board[i][j-1] == 0 and board[i-1][j] == 0 : 
                d[(1,i,j)] = d[(0,i-1,j-1)] + d[(1,i-1,j-1)]  + d[(2,i-1,j-1)]
            
    
print(sum([d[(i,N-1,N-1)] for i in range(3)]))