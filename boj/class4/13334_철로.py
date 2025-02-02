# 정렬 + 슬라이딩 윈도우
# 윈도우는 시작점을 기준으로 이동, 윈도우에 들어오는 친구들은 힙으로 관리 (끝점 max heap)
# 윈도우는 새 친구가 들어오지 못할 때 이동 윈도우가 이동할떄 힙에서 제거, 

import sys
import heapq
input = sys.stdin.readline

n = int(input())
ho, heap = [], []
for _ in range(n): 
    ho.append(sorted([int(x) for x in input().split()]))
d = int(input())

ho.sort(key=lambda x:(x[0], -x[1]))

window_start, answer = 0, 0

for h,o in ho :
    if o - h > d : # 규격보다 큰 경우
        continue
    
    if o > window_start + d : # 그냥 추가가 안되는 경우 -> 힙에서 지우고 이동
        while heap and o > heap[0] + d:
            heapq.heappop(heap)
        if heap : 
            window_start = heap[0]
        else : 
            window_start = h

    heapq.heappush(heap, h)            
    answer = max(answer, len(heap))

print(answer)