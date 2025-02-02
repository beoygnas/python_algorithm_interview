# 순환을 찾는 문제
# 각 칸을 순회하면서, dfs + union-find

N, M = [int(x) for x in input().split()]
board = [[ch for ch in input()] for _ in range(N)]
dir = {
    'U':(-1,0),
    'D':(1,0),
    'L':(0,-1),
    'R':(0,1)
}
    
root = {(i,j):(i,j) for i in range(N) for j in range(M)}

for i in range(N):
    for j in range(M):
        root[(i,j)] = (i,j)

def find(x):
    if x == root[x] :
        return x
    else :
        return find(root[x])
    
def union(x, y): 
    a, b = find(x), find(y)
    if a < b :
        root[b] = a
    else :
        root[a] = b

def dfs(x,y):
    nxt_dir = dir[board[x][y]]
    nx,ny = x+nxt_dir[0], y+nxt_dir[1] 
    if find((x,y)) == find((nx, ny)):
        return
    else :
        union((x,y), (nx,ny))
        dfs(nx, ny)


answer = set()         
for i in range(N):
    for j in range(M):
        dfs(i,j)
        answer.add(find((i,j)))
        
print(len(answer))
