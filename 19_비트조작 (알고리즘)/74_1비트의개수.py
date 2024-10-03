# https://leetcode.com/problems/number-of-1-bits

# 0. 파이썬 내장함수 이용 O(n)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    

# 1. log(N)에 하는 방법
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        answer = 0
        while n :
            if n % 2 : 
                answer += 1
            n = n//2
        return answer
    
# 2. 비트연산을 활용하는 방법
class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n :
            n &= n - 1
            answer += 1
        return answer