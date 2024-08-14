# https://leetcode.com/problems/combinations
from typing import * 
import itertools


# 0. 재귀
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        results, used = [], [0] * (n+1)

        def dfs(elements, start) :
            if len(elements) == k :
                results.append(elements[:])
                return 
            
            for i in range(start, n+1) : 
                if used[i] == 0 :
                    used[i] = 1
                    elements.append(i)
                    dfs(elements, i+1)
                    used[i] = 0
                    elements.pop()

        dfs([], 1)
        return results
        
        

# 1. 파이썬
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations([_ + 1 for _ in range(n)], k))
    
# 1-1. 굳이 range를 list로 바꿀 필요 없음    
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = itertools.combinations(range(1, n+1), k)
        return answer
        
# 2. used를 굳이 쓸 필요가 없음. 정렬되 있고, 1씩 증가하는 함수이기 떄문에.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def dfs(elements, start) :
            if len(elements) == k : 
                answer.append(elements[:])
                return 

            for i in range(start, n+1) : 
                elements.append(i)
                dfs(elements, i+1)
                elements.pop()

        dfs([], 1)
        return answer