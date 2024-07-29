# https://leetcode.com/problems/product-of-array-except-self

from typing import * 

# 0. 왼쪽배열 * 오른쪽 배열, 풀이 봤음.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 나눗셈은 곧 뺼셈?
        l, r = [1], [1]

        for i in range (len(nums) - 1) : 
            l.append(l[i] * nums[i])
            r.append(r[i] * nums[len(nums)-1 - i])
        
        answer = []
        for i in range(len(nums)) : 
            answer.append(l[i] * r[len(nums) - 1 - i])

        return answer
    
# 1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 나눗셈은 곧 뺼셈?
        out = []
        p = 1

        for i in range(0, len(nums)) : 
            out.append(p)
            p *= nums[i]
        p = 1
        for i in range(0, len(nums)):
            out[len(nums)-1 - i] *= p
            p *= nums[len(nums)-1 - i]
        
        return out