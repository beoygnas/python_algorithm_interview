# 지금 보고 있는 애보다 큰 게 나올때까지 window 치기
# stack인 거 같은데
# deque?

# 누적합으로 유지하는 방법이 뭐있을까

# 그리디였음 : 도킹할때, 가장 비어있는 애들 중에 가장 큰 값으로
# 비어있는 거 찾는건, union-find를 통해 O(1)
import sys
input = sys.stdin.readline

G, P = int(input()), int(input())
p = [i for i in range(G+1)]

def find(x) :
    if x != p[x] :
        p[x] = find(p[x])
    return p[x]

def union(x, y) :
    p[find(y)] = find(x)

planes = [int(input()) for _ in range(P)]
answer = 0
for plane in planes:
    plane = find(plane)
    if plane == 0 : 
        break
    union(plane-1, plane)
    answer += 1
    
print(answer)
