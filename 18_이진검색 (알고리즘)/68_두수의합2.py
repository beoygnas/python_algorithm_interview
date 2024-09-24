# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

# 0. O(nlogn), 하나씩 binary search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers) :
            index = bisect.bisect_left(numbers, target - num) 
            if index < len(numbers) and numbers[index] == target - num and index != i:
                return [min(i, index) + 1, max(i, index) + 1]
            
# 1.  O(n) 투포인터
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(nlogn), 하나씩 binary search
        # O(n) 투포인터

        i, j = 0, len(numbers) - 1
        
        while i < j : 
            if numbers[i] + numbers[j] > target : 
                j -= 1
            elif numbers[i] + numbers[j] < target : 
                i += 1
            else : 
                return i+1, j+1

# 2. bisect, 슬라이싱 없이
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers) :
            index = bisect.bisect_left(numbers, target - num, i+1) 
            if index < len(numbers) and numbers[index] == target - num : 
                return i+1, index+1
            