# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import * 

# 0. 재귀 이용
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        answer = []
        digit_dict = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        def dfs(sub_digits: str) : 
            if len(sub_digits) == len(digits) : 
                if sub_digits != "" : 
                    answer.append(sub_digits)
                return
            
            digit = digits[len(sub_digits)]

            for char in digit_dict[digit] : 
                dfs(sub_digits + char)

        dfs("")
        return answer 
    
# 1. 좀더 깔끔하게
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        answer = []
        digit_dict = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }

        def dfs(index, sub_digits: str) : 
            if len(sub_digits) == len(digits) : 
                if sub_digits != "" : 
                    answer.append(sub_digits)
                return
            
            for char in digit_dict[digits[index]] : 
                dfs(index+1, sub_digits + char)

        dfs(0, "")
        return answer 