# https://leetcode.com/problems/single-number
import collections
# 0. counter를 쓴 뻔한 풀이
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common()[-1][0]

# 1. XOR로 들어온 친구는 XOR로만 나갈 수 있다는 풀이
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums :
            result ^= num
        return result
