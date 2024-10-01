# https://leetcode.com/problems/majority-element/
import collections

# 0. 절반을 초과하는 게 무조건 있으므로, 그냥 가장 많은 값을 return
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]

# 1. 일일이 확인하여 return
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for k in counter : 
            if counter[k] > len(nums)//2 :
                return k
            
# 2. dp로 최적화 (앞선 구조를 재사용함)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = collections.defaultdict(int)
        for n in nums :
            counter[n] += 1
            if counter[n] > len(nums) // 2 :
                return n

# 3. 분할 정복 (O(nlogn))
# dp로 최적화
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums : 
            return None 
        if len(nums) == 1 :
            return nums[0]
        
        # 분할
        half = len(nums)//2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        # 정복 
        return [b,a][nums.count(a) > len(nums) // 2]
    
# 4. 무조건 과반수 이상으로 있으므로, 정렬하고 과반수 indexing
# O(nlogn)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
