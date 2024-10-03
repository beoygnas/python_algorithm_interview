# https://leetcode.com/problems/maximum-subarray

# 0. O(n^2)에 푸는 풀이
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # d[i][j] : i ~ j 까지 최대 합.
        n = len(nums)
        d = [[0] * n for _ in range(n)]
        d[0][0] = nums[0]

        answer = d[0][0]

        for i in range(0, n) :
            d[0][i] = nums[i] + d[0][i-1]
            answer = max(answer, d[0][i])
        
        for i in range(1, n) :
            for j in range(i, n) : 
                if j==i : 
                    d[i][j] = nums[j]
                else :
                    d[i][j] = max(d[i-1][j], d[i][j-1]+nums[j])
                    answer = max(answer, d[i][j])
        
        return answer
        
# 0-1. O(n) 풀이
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        d = collections.defaultdict(int)
        d[0] = answer = nums[0]
        
        for i in range(1, len(nums)) :
            d[i] = max(d[i-1]+ nums[i], nums[i])
            answer =  max(d[i], answer)

        return answer

# 0-2. 변수를 최소화 
# d[n] : n까지 왔을 때 최대 합
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        x = answer = nums[0]
        for i in range(1, len(nums)) :
            x = max(x+ nums[i], nums[i])
            answer =  max(x, answer)

        return answer
        
# 1.메모이제이션
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)) :
            nums[i] += max(nums[i-1] + nums[i], nums[i])
        return max(nums)
