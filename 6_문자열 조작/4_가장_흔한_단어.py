# https://leetcode.com/problems/most-common-word/

import collections
import headpq
import functools
import itertools
import re   
import sys
import math
import bisect
from typing import * 

# 내가 푼 풀이
# 빠르지만, 살짝 c++ 느낌나고 어거지로 푼 느낌.
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = [word.lower() for word in banned] 
        counter = collections.defaultdict(int)
        word = ""
        for ch in paragraph + '.' :
            if not ch.isalpha() : 
                if word != "" : counter[word] += 1
                word = ""
            else :
                word += ch.lower()

        max_values = -1
        max_word = ""

        for k, v in counter.items() :
            if v > max_values and k not in banned : 
                max_values = v
                max_word = k 
        
        return max_word

# 1. 리스트 컴프리헨션, Counter 객체 사용
# 같은 풀이이지만 , 리스트 컴프리헤션 및 Counter로 조금 더 파이썬 스럽다.
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = ''.join([ch.lower() if ch.isalpha() else ' ' for ch in paragraph ]).split()
        banned = [word.lower() for word in banned]
        counter = collections.Counter(paragraph)

        max_value = -1
        max_key = ''

        for k,v in counter.items() : 
            if v > max_value and k not in banned and k != "" : 
                max_value = v
                max_key = k

        return max_key

# 2. regex를 적용, counter 객체의 most_common() 을 이용하여 더 쉽게
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^a-zA-Z]', ' ',  paragraph)
        paragraph = paragraph.lower().split()
        words = [word for word in paragraph if word not in banned]
        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]
