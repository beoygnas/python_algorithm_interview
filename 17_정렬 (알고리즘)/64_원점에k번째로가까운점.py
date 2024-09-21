# https://leetcode.com/problems/k-closest-points-to-origin

# 0. 힙을 이용한 풀이
# heap 쓰면 최단시간일 듯 한데 => nope, n log n 
# bst도 여도 nlogn 일듯 
# sort도 n log n 
import heapq
from typing import * 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        
        for x, y in points : 
            distance = x**2 + y**2
            heapq.heappush(heap, (distance, (x,y)))
        
        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])

        return answer

# 0-1. 정렬
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]