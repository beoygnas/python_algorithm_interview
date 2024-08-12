# https://leetcode.com/problems/number-of-islands 
from typing import * 

# 0. 스택을 이용
# dx, dy, visited 등 c++에서 하던 습관 그대로 유지되서 별로.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        dx, dy = [1,0, -1, 0], [0, 1, 0, -1]
        answer = 0
        
        for i in range(m) :
            for j in range(n) :
                if visited[i][j] == 0 and grid[i][j] == '1' : 
                    stack = [(i, j)]
                    answer += 1
                    while stack : 
                        cur = stack.pop()
                        a, b = cur[0], cur[1]
                        if visited[a][b] == 0 : 
                            visited[a][b] = 1 
                            for x, y in zip(dx, dy) : 
                                nx, ny = a + x, b + y
                                if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == '1': 
                                    stack.append((nx, ny))
                                    print(nx, ny)

        return answer

# 1. 재귀 이용
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        dxs, dys = [1,0,-1,0], [0,1,0,-1]
        self.answer = 0

        def dfs(x:int, y:int) : 
            if x < 0 or x >= m or y < 0 or y>=n or grid[x][y] != '1' or visited[x][y] == 1 :
                return 
            visited[x][y] = 1
            for dx,dy in zip(dxs, dys) :     
                dfs(x + dx, y + dy)

        for i in range(m) : 
            for j in range(n) : 
                if grid[i][j] == '1' and visited[i][j] == 0 :
                    print(i, j)
                    dfs(i, j)
                    self.answer  += 1

        return self.answer

# 2. 재귀 베이스에, 불필요한 공간/시간 복잡도 제거
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        answer = 0

        def dfs(x:int, y:int) : 
            if x < 0 or x >= m or y < 0 or y>=n or grid[x][y] != '1' :
                return 
                
            grid[x][y] = '0'
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x-1, y)
            dfs(x, y-1)

        for i in range(m) : 
            for j in range(n) : 
                if grid[i][j] == '1' :
                    dfs(i, j)
                    answer  += 1

        return answer
