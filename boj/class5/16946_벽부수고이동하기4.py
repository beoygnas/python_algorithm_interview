# BFS
# 0인 칸에서 BFS를 하면서 path들을 저장, path마다 총 개수를 저장해놓음.
# BFS를 다돌면, 1인칸에서는 인접한 애들의 값 + 1 로 업데이트
# path_id를 중간에 생각했는데, 미리 생각해야할듯

import collections

N, M = [int(x) for x in input().split()]
board = [[0] * M for _ in range(N)]
counts = [[(0,0)] * M for _ in range(N)]
dx, dy = [1,0,-1,0], [0,1,0,-1]
vis = collections.defaultdict(int)


for i in range(N):
    for j, ch in enumerate(input()):
        board[i][j] = int(ch)
        
def OOB(x, y):
    return x<0 or x>=N or y<0 or y>=M

def bfs(x, y, path_id):
    paths = [(x,y)]
    vis[(x,y)] = 1
    q = collections.deque([(x,y)])

    while q :
        cx, cy = q.popleft()
        for dir in range(4) :
            nx, ny = cx+dx[dir], cy+dy[dir]
            if not (OOB(nx, ny) or vis[(nx,ny)]) and board[nx][ny] == 0:
                vis[(nx, ny)] = 1
                q.append((nx, ny))
                paths.append((nx,ny))


    path_vis = collections.defaultdict(int)
    for px,py in paths :
        counts[px][py] = (len(paths), path_id)
        for dir in range(4): 
            nx, ny = px+dx[dir], py+dy[dir]
            if not OOB(nx, ny) and board[nx][ny] and path_vis[(nx, ny)] == 0:
                board[nx][ny] += len(paths)
                path_vis[(nx, ny)] = 1
    
path_id = 1
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 0 and not vis[(i,j)]:
            bfs(i, j, path_id)
            path_id += 1
            
for i in range(N) :
    row = ''
    for num in board[i] :
        row += str(num%10)
    print(row)
