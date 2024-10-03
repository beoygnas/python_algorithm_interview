# https://leetcode.com/problems/fibonacci-number
import collections

# 0. 상향식, tabulation 풀이
class Solution:
    def fib(self, n: int) -> int:
        d = collections.defaultdict(int)
        d[0], d[1] = 0, 1
        for i in range(2, n+1) :
            d[i] = d[i-1] + d[i-2]
        return d[n]
    
# 1. 하향식, memoizaion
class Solution:
    d = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        
        if n<=1 : 
            return 1
        
        if self.d[n] == 0 :
            self.d[n] = self.fib(n-1) + self.fib(n-2)
        return self.d[n]


# 2. 변수 2개로만 가능, 천재다..
class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(n) :
            x,y = y, x+y
        return x