# dfs
import collections
A, B = [int(x) for x in input().split()]

answer = float('inf')

def dfs(n, cnts) : 
    global answer
    if n == B : 
        answer = min(answer, cnts)
    elif n > B : 
        return
    else : 
        dfs(n*2, cnts+1)
        dfs(n*10+1, cnts+1)

dfs(A, 1)
print(answer if answer != float('inf') else -1)
    
    
    
    