# https://leetcode.com/problems/subsets
from typing import * 
import itertools

# 0. 중복순열로 구한후, set 연산
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def fun(elements, index) : 
            
            answer.append(tuple(elements))
            if index == len(nums) : 
                return 
            
            for i in range(index, len(nums)) : 
                fun(elements + [nums[i]], i+1)

        fun([],0)
        return set(answer)
    

# 1. set이 없어도 오케이? 
# All the numbers of nums are unique. 이어서 가능
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # 중복순열로 구한후, set 연산
        answer = []
        def fun(elements, index) : 
            
            answer.append(elements)
            
            for i in range(index, len(nums)) : 
                fun(elements + [nums[i]], i+1)

        fun([],0)
        return answer