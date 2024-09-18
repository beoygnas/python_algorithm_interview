# https://leetcode.com/problems/merge-intervals

from typing import * 

# 0. 투포인터, n log n
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 정렬 후 한번 탐색하면 될 듯.
        # 정렬은 그냥 오름차순
        answer = []
        intervals.sort()
        l, r = 0, 0

        while l < len(intervals) and r < len(intervals): 
            
            if intervals[l][1] >= intervals[r][0] :
                intervals[l][1] = max(intervals[r][1], intervals[l][1])
                r += 1
            else : 
                answer.append(intervals[l])
                l = r

        answer.append(intervals[l])

        return answer

# 1. 같은 풀이, but 좀 더 최적화
# 불필요한 변수 제거 및 lambda 활용
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in sorted(intervals, key = lambda x: x[0]) : 
            if answer and i[0] <= answer[-1][1] : 
                answer[-1][1] = max(answer[-1][1], i[1])
            else : 
                answer.append(i)
        
        return answer
            