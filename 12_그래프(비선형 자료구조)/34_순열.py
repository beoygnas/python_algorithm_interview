# https://leetcode.com/problems/permutations
from typing import * 
import itertools

# 0. 재귀와 index를 이용한 순열 순회
# index used 배열을 이용하여, 현재 보고 있는 놈이 사용했는지를 체크함.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer, used = [], [0] * 6
        
        def dfs(sub_list : List[int]) : 
            if len(sub_list) == len(nums) : 
                answer.append([nums[i] for i in sub_list])
                return
            
            for i in range(len(nums)) : 
                if not used[i] :
                    used[i] = 1
                    sub_list.append(i)
                    dfs(sub_list)
                    used[i] = 0
                    sub_list.pop()
        
        dfs([])
        return answer


# 1. 재귀 및 python list를 이용한 구현
# 배열 크기가 작아 remove 시간이 적긴해도, 안좋길 할 것.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer, prev_elements = [], []
        
        def dfs(elements) : 
            if len(elements) == 0 : 
                answer.append(prev_elements[:])

            for e in elements : 
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return answer


# 2. itertools 라이브러리 이용

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
