# 누굴 먼저 올리느냐에 따라, truth에 포함이 안될 수 있다
# union find로 하면 해결됨.

import collections

N,M = [int(x) for x in input().split()]
K = [int(x) for x in input().split()]

parent = {i:i for i in range(1, N+1)}
party = collections.defaultdict(list)

def find(x) : 
    if parent[x] != x :
        x = find(parent[x])
    return x

def union(x, y):
    parent[find(x)] = find(y)

if K[0] == 0 : 
    print(M)
else : 
    for i in K[1:]:
        parent[i] = K[1]

    for i in range(M) : 
        party[i] = [int(x) for x in input().split()][1:]
        for j in range(1, len(party[i])):
            union(party[i][0], party[i][j])
        
    answer = 0 
    for i in party : 
        if all([find(p) != find(K[1]) for p in party[i]]) : 
            answer += 1 

    print(answer)