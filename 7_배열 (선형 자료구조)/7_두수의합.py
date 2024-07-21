# https://leetcode.com/problems/two-sum/
# Set
import collections
from typing import * 

# 0. 내가 푼 풀이
# 지저분한 투포인터 풀이 : O(n log n), 너무 지저분하고 귀찮아질 것 같을 땐 다른 풀이를 생각해보자.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        l, r = 0, len(nums) - 1
        
        while sorted_nums[l] + sorted_nums[r] != target : 
            if sorted_nums[l] + sorted_nums[r] > target :
                r -= 1
            else :
                l += 1
        ans_l, ans_r = -1, -1
        if sorted_nums[l] != sorted_nums[r] :
            ans_l, ans_r = nums.index(sorted_nums[l]), nums.index(sorted_nums[r])
        else : 
            for i, n in enumerate(nums) : 
                if n == sorted_nums[l] : 
                    
                    if ans_l != -1 :
                        ans_r = i
                        return ans_l, ans_r
                    else :
                        ans_l = i

        return ans_l, ans_r

# 1. in을 이용한 탐색
# 일반 brute force 보다는 성능이 좋지만, 통과는 못함.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums) : 
            if target - num in nums[i+1:] : 
                return [i, nums[i+1:].index(target-num) + (i+1)]
            
# 2. 첫 번째 수를 뺀 결과 키 조회
# hash table 을 이용하여, O(n)에도 가능
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i, num in enumerate(nums) : 
            if target - num in sum_dict :
                return [i, sum_dict[target - num]]
            else : 
                sum_dict[num] = i
