# https://leetcode.com/problems/sum-of-two-integers

# 0. 전가산기를 구현, 비트연산에 대해 잘 알아야함.
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0X7FFFFFFF
        
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        sum = 0
        for i in range(32) :
            A = int(a_bin[31-i])
            B = int(b_bin[31-i])
    
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry 
            sum = Q2 ^ carry
            carry = Q1 | Q3
            
            result.append(str(sum))
        
        if carry == 1 :
            result.append('1')
        
        # 초과 자릿수 : 32 bit로 만들어주기
        result = int(''.join(result[::-1]), 2) & MASK
        
        # 음수 처리
        if result > INT_MAX :
            result = ~(result ^ MASK)
        return result 