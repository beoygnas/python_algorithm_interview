# https://leetcode.com/problems/combination-sum
from typing import * 
import itertools

# 0. backtracking + 중복조합, 재귀시 자기자신 idx 포함
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def fun(elements, idx, sum) : 
            if sum == target : 
                answer.append(elements[:])
            if sum >= target : 
                return

            for i in range(idx, len(candidates)) : 
                elements.append(candidates[i])
                fun(elements, i, sum+candidates[i])
                elements.pop()
                
                # fun(elements + [candidates[i]], i, sum+candidates[i])

        fun([], 0, 0)
        return answer
            

# 1. 더하면서 가는게 아니라, 뺴면서 가는것도 고려
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        answer = []
        
        def fun(csum, index, path) : 
            if csum == 0 : 
                answer.append(path)
            if csum <= 0 : 
                return 
            for i in range(index, len(candidates)) : 
                fun(csum-candidates[i], i, path + [candidates[i]])

        fun(target, 0, [])
        return answer
            

