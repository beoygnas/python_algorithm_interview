# https://leetcode.com/problems/kth-largest-element-in-an-array/

# 0. heap 모듈을 이용

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []
        for n in nums : 
            heapq.heappush(heap, -n)
        
        for _ in range(k-1) :
            heapq.heappop(heap)
            
        return -1 * heap[0]
    
# 1. heap 모듈의 heapfiy 이용        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        
        for _ in range(len(nums) - k) :
            heapq.heappop(nums)
    
        return nums[0]
        

# 2. heapq 모듈의 nlargest 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


# 3. 정렬 : 내부 구현이 C여서 가장 빠름.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
        
        