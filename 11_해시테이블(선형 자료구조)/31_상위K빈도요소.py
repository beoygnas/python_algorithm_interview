# https://leetcode.com/problems/top-k-frequent-elements

import collections, heapq
from typing import *

# 0. 꽤 파이썬스럽게 풀었음 O(nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        return [item[0] for item in sorted(counter.items(), key=lambda x:x[1])][-k:]
    
# 1. 우선순위큐, heap push/pop O(n log n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # heapq를 이용
        counter = collections.Counter(nums)
        heap = []

        for num in counter : 
            # item (-1 * 빈도, 숫자) -> 내림차순을 위해
            heapq.heappush(heap, (-counter[num] , num))

        answer = []    
        for _ in range(k) :
            answer.append(heapq.heappop(heap)[1])

        return answer

# 2. 더 파이썬
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in collections.Counter(nums).most_common(k)]

# 3. zip 모듈 이용
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in collections.Counter(nums).most_common(k)]
    
