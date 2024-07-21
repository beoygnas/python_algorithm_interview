import collections
import headpq
import functools
import itertools
import re   
import sys
import math
import bisect
from typing import * 

# 0. 내가 푼 풀이, list reverse() 이용 
# 2. 파이썬 스럽게 풀기
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        
# 1. 내가푼 풀이투포인터
class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        length = len(s)
        for i in range(0, length/2) : 
            tmp = s[i]
            s[i] = s[length - i - 1]
            s[length - i - 1] = tmp
            
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right :
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        