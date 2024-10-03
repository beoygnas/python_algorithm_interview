# https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        # d[n] : n까지 왔을 때 최대 훔친돈

        if len(nums) <= 2 :
            return max(nums)
        
        nums[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)) :
            nums[i] = max(nums[i-2]+nums[i], nums[i-1])
            
        return nums[len(nums)-1]

