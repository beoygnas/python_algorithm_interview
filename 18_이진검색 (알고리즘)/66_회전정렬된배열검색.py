# https://leetcode.com/problems/search-in-rotated-sorted-array

# 0. 바뀌는 부분을 파라메트릭 서치로, 이진검색
# 왼쪽을 기준으로 했기 때문에 구현이 더 복잡했음.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 1. l < r 이 바뀌는 지점을 찾는다 (log n)
        l, r, offset = 0, len(nums) - 1, 0
    
        while l <= r : 
            mid = (l+r) // 2   
            if nums[l] <= nums[mid] : 
                if mid+1 < len(nums) and nums[mid] > nums[mid+1] :
                    offset = mid + 1
                l = mid + 1
            else : 
                r = mid - 1

        rotated_nums = nums[offset:] + nums[:offset]
        index = bisect.bisect_left(rotated_nums, target)
        if index < len(nums) and rotated_nums[index] == target:
            return (index + offset) % len(nums)
        else : 
            return -1

        
# 1. 최소값인 피벗을 오른쪽을 기준으로 찾는다!
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
    
        while l < r : 
            mid = l+ (r - l) // 2   
            if nums[mid] > nums[r] :
                l = mid + 1
            else :
                r = mid
        
        offset = l

        rotated_nums = nums[offset:] + nums[:offset]
        index = bisect.bisect_left(rotated_nums, target)
        if index < len(nums) and rotated_nums[index] == target:
            return (index + offset) % len(nums)
        else : 
            return -1



        
        
        
        



        
        
        
        
