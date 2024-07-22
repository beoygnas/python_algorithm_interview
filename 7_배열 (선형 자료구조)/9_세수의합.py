# https://leetcode.com/problems/3sum/

# 정렬 후 투포인터로 n^2에 가능할듯.
# 정렬 후 해쉬로 n^2에 가능
# 브루트포스로 n^3에도 가능

from typing import * 

# 0. 내가 푼 풀이, 순회 + 투포인터
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        nums.sort()
        for i, num in enumerate(nums) : 
            # 중복 제거로 빠른 시간 단축이 가능
            if i > 0 and num == nums[i-1] :
                continue
            l, r = i+1, len(nums) - 1
            while(l<r) : 
                if nums[l] + nums[r] + num == 0 :
                    solutions.add(tuple([nums[l], nums[r], num]))
                    while l<r and nums[l] == nums[l+1] : l += 1
                    while l<r and nums[r] == nums[r-1] : r -= 1
                if nums[l] + nums[r] + num > 0 : 
                    r -= 1
                else : 
                    l += 1 

        return [list(sol) for sol in solutions]

# 1. 순회 + hash 순회
# 어거지로 짠 hash 순회, 중복제거를 하지 않으면, timeout

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        nums.sort()
        for i, num1 in enumerate(nums) : 
            if i>0 and nums[i] == nums[i-1] : continue
            target = num1 *-1 
            nums_map = {}
            for j, num2 in enumerate(nums[i+1:]) : 
                if target - num2 in nums_map :
                    solutions.add(tuple(sorted([num1, num2, target-num2])))
                nums_map[num2] = j
        return solutions