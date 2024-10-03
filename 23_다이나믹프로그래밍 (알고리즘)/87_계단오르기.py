# https://leetcode.com/problems/climbing-stairs
import collections

# 0. 타뷸레이션, [n] = n 까지 가는데 방법 개수
class Solution:
    def climbStairs(self, n: int) -> int:
        d = collections.defaultdict(int)
        d[0], d[1] = 1, 1
        for i in range(2, n+1) :
            d[i] = d[i-1] + d[i-2]
        return d[n]

# 1. 메모이제이션 방법
class Solution:
    d = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n <= 2 : 
            return n
        if self.d[n] == 0 : 
            self.d[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.d[n]

