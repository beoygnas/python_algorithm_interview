# https://leetcode.com/problems/trapping-rain-water/

import collections
from typing import * 


# 0. stack으로 접근했지만, 못풀었음.
# distance 및 stack의 원소로 index에 대해 생각하지 못했음.


# 1. 투 포인터를 최대로 이동
# 각자의 영역에서 투포인터를 옮기면서, 답을 채운다.
# 투포인터 둘중 하나는 언젠가 최대 높이를 찾을 거고, 그거는 ascending 할 것.
# 그러므로, 두 투포인터를 계속 비교해가면서 높은 쪽으로 이동하면 된다.
class Solution:
    def trap(self, height: List[int]) -> int:
        
        answer = 0
        l, r = 0, len(height) - 1 
        l_max, r_max = height[l], height[r]

        while l < r :
            l_max, r_max = max(height[l], l_max), max(height[r], r_max)

            if l_max < r_max : 
                answer += l_max - height[l]
                l += 1 
            else : 
                answer += r_max - height[r]
                r -= 1

        return answer

# 2. 스택 쌓기 방식.
class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack = []
        answer = 0

        for i,h in enumerate(height) : 

            distance = 0
            while stack and h > height[stack[-1]] : 
                top = stack.pop()            
                if len(stack) == 0 : break
                distance = i - stack[-1] - 1
                rain = min(height[i], height[stack[-1]]) - height[top]
                answer += rain *  distance

            stack.append(i)

        return answer



