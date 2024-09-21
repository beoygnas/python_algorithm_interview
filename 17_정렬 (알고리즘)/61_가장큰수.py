# https://leetcode.com/problems/largest-number
from functools import cmp_to_key
from typing import * 

# 0. cmp_to_key를 이용한 custom function
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x1, x2) -> bool :
            if x1+x2 < x2+x1 : 
                return 1
            else : 
                return -1 

        nums = [str(num) for num in nums]
        nums = sorted(nums, key = cmp_to_key(cmp))
        return str(int(''.join(nums)))

# 1. insertion_sort + cmp function
class Solution:
    def cmp(self, n1, n2) : 
        return str(n1)+str(n2) < str(n2)+str(n1)

    def largestNumber(self, nums: List[int]) -> str:
        
        i = 1
        while i < len(nums) : 
            j = i
            while j > 0 and self.cmp(nums[j-1], nums[j]) : 
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1
        
        return str(int(''.join(map(str, nums))))
