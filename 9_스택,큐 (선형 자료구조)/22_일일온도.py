# https://leetcode.com/problems/daily-temperatures/description/
import collections
from typing import * 

# 0. stack에 day 정보까지 쌓는다.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack에 day 정보까지
        stack, ans = [], [0] * len(temperatures)

        for i, t in enumerate(temperatures) : 
            while stack and t > stack[-1][1] : 
                top = stack.pop()
                ans[top[0]] = i - top[0]
            stack.append((i, t))
        
        return ans

# 1. 굳이 stack에 tuple로 추가할 필요는 없다.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack에 day 정보까지
        stack, ans = [], [0] * len(temperatures)

        for i, t in enumerate(temperatures) : 
            while stack and t > temperatures[stack[-1]]: 
                top = stack.pop()
                ans[top] = i - top
            stack.append(i)
        
        return ans