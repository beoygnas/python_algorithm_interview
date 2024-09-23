# https://leetcode.com/problems/binary-search

from typing import * 

# 0. 재귀
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(l, r) : 
            if l > r : return -1
            mid = (l+r) // 2
            
            if nums[mid] > target : 
                return binary_search(l, mid - 1)
            elif nums[mid] < target : 
                return binary_search(mid + 1, r)
            else :
                return mid
            
        return binary_search(0, len(nums)-1)

# 1. 반복
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        while l <= r : 
            mid = (l+r)//2
            if nums[mid] == target : 
                return mid
            elif nums[mid] < target : 
                l = mid + 1
            else : 
                r = mid - 1
        
        return -1

