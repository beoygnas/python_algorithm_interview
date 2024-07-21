# https://leetcode.com/problems/group-anagrams/
# Set
import collections
from typing import * 

# 0. 내가 푼 풀이
# n^3, 모든 경우를 정석대로 체크
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestpalindrome = s[0]
        for i in range(len(s)) : 
            for j in range(i+1, len(s)+1) : 
                substr = s[i:j]
                if substr == substr[::-1] and j-i > len(longestpalindrome):
                    longestpalindrome = substr
        return longestpalindrome
    
    
# 1. 중앙을 중심으로 확장하는 풀이
# n^2에 가능할듯, 중앙 인덱스를 옮기면서 투포인터로

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while(l >= 0 and r < len(s) and s[l] == s[r]) : 
                l -= 1
                r += 1
            return s[l+1:r]
        longest_palindrome = ""
        for i in range(len(s)) :    
            longest_palindrome = max(expand(i,i), expand(i,i+1), longest_palindrome, key=len)    

        return longest_palindrome