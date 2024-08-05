# https://leetcode.com/problems/longest-substring-without-repeating-characters

import collections
from typing import *

# 0. 투포인터 + hash table
# 이전 index를 유지하다보니 이상해짐.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 순회하면서 hash table을 유지
        # 투 포인터
        idx_dict, prev_idx, answer = {}, -1, 0

        for i, ch in enumerate(s) :
            if ch in idx_dict and idx_dict[ch] != -1 : 
                cur = idx_dict[ch]
                for char in s[prev_idx+1:cur+1] : 
                    idx_dict[char] = -1
                prev_idx = cur
        
            answer = max(answer, i - prev_idx)
            idx_dict[ch] = i
        return answer
    

# 1. 슬라이딩 윈도우와 투 포인터로 사이즈 조절
# 비슷한 아이디어지만, 예외처리를 하는 데에 있어서 훨씬 간결하게 표현
# 나는 이전 idx 부터 현재까지 모두보며 dict를 -1으로 처리하는 반복문을 추가했지만,
# index 의 위치로 아예 고려하지 않는 방법도 있음.   
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 순회하면서 hash table을 유지
        # 투 포인터

        idx_dict = {}
        answer = start = 0

        for i, ch in enumerate(s) :
            if ch in idx_dict and start <= idx_dict[ch] :
                start = idx_dict[ch] + 1
            
            answer = max(answer, i - start + 1)
            idx_dict[ch] = i

        return answer