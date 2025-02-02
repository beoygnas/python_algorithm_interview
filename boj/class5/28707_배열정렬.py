# 백트래킹
# 현재 상태를 메모이제이션으로 풀이
# 매번 state 마다 할 수 있는거 다하기, 모든 state를 딱 한번씩 방문

# 시간복잡도 8! * 10 (따지기)
# swap + tuple로 바꾸기 = 2 + 10
# 영원히 할 수도 있지만, 결국, func()을 작동시키는건 8^8 밖에 못함.
import collections 
import heapq

N = int(input())
A = [int(x) for x in input().split()]
M = int(input())
lrc = [[int(x) for x in input().split()] for _ in range(M)]

def is_ascending(t) :
    for i in range(1, N) :
        if t[i] < t[i-1] :
            return False
    return True

d = collections.defaultdict(int)
answer = float('inf')

pq = [(0, tuple(A))]

while pq : 
    price, cur = heapq.heappop(pq)
    
    if cur in d and price >= d[cur]:
        continue
    d[cur] = price
    if is_ascending(cur) :
        answer = min(answer, price)
    
    for l,r,c in lrc : 
        nxt = list(cur)
        nxt[l-1], nxt[r-1] = nxt[r-1], nxt[l-1]
        nxt = tuple(nxt)
        if nxt not in d or (nxt in d and price+c < d[nxt]):
            heapq.heappush(pq, (price+c, nxt))


print(-1 if answer == float('inf') else answer)