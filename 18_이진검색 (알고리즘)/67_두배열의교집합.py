# https://leetcode.com/problems/intersection-of-two-arrays/
import bisect

# 0. 정렬로 binary search가 가능하도록
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # n log n
        nums1.sort()
        nums2.sort()
        answer = set()
        
        for n in nums1 : 
            index = bisect.bisect_left(nums2, n)
            if index < len(nums2) and nums2[index] == n : 
                answer.add(n)

        for n in nums2 : 
            index = bisect.bisect_left(nums1, n)
            if index < len(nums1) and nums1[index] == n : 
                answer.add(n)

        return list(answer)

# 1. 한 리스트만 정렬을 해도 된다.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # n log n
        nums2.sort()
        answer = set()
        
        for n in nums1 : 
            index = bisect.bisect_left(nums2, n)
            if index < len(nums2) and nums2[index] == n : 
                answer.add(n)

        return list(answer)
    
# 2. 두 리스트를 모두 정렬 후 투포인터로
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # n log n
        nums1.sort()
        nums2.sort()
        answer = set()
        
        i = j = 0
        while i < len(nums1) and j < len(nums2) : 
            if nums1[i] > nums2[j] : 
                j += 1
            elif nums1[i] < nums2[j] : 
                i += 1
            else : 
                answer.add(nums1[i])
                i += 1
                j += 1
                

        return list(answer)