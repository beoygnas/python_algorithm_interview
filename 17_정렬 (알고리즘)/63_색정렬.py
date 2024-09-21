# https://leetcode.com/problems/sort-colors

# 0. 단순 정렬
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()
        
# 0-1. counter 이용
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = collections.Counter(nums)
        
        i = 0
        for _ in range(len(nums)) : 
            while counter[i] == 0 : 
                i += 1
            nums[_] = i
            counter[i] -= 1
            
# 1. 네덜란드 국기문제를 응용한 풀이, 3 partitioning
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)

        while white < blue : 
            if nums[white] == 0 :
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1 :
                white += 1
            elif nums[white] == 2 :
                blue -= 1
                nums[blue], nums[white] = nums[white], nums[blue]

