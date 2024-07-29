# https://leetcode.com/problems/array-partition/

from typing import * 

# 0. 정렬해놓고 하나씩 고르기.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::2]
        return sum(nums)

# 1. 좀더 파이썬스럽게
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return sum(sorted(nums)[::2])