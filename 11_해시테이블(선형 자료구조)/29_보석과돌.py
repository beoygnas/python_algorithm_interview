# https://leetcode.com/problems/jewels-and-stones

import collections
from typing import *

# 0. 간단하게 Counter 사용 : O(m)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        counter = collections.Counter(jewels)
        for stone in stones : 
            if stone in counter : 
                answer += 1

        return answer
    
# 1. 반대로 Counter 하는게 훨씬 굿 O(m)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        answer = 0
        counter = collections.Counter(stones)
        for jewel in jewels :
            answer += counter[jewel]
    
        return answer

# 2. 파이썬스러운 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)