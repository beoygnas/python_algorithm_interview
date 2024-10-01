from typing import * 

# 정렬하고 원하는 인덱스에 넣어주기.
# 0. h, k 순서대로 정렬하고 나오면, 원하는 인덱스에 서면됨 (그리디) 
# 정렬한다음에 서면 뒤에 어떻게되든 영향을 미치지 않으니까.
import heapq
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for p in people : 
            heapq.heappush(heap, (-p[0], p[1]))
        result = []
        while heap :
            p = heapq.heappop(heap)
            print(p) 
            result.insert(p[1], [-p[0], p[1]])
        

        return result 
            

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        
        people.sort(key=lambda x:(-x[0], x[1]))
        for p in people :
            result.insert(p[1], p)

        return result 
            