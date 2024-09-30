# https://leetcode.com/problems/minimum-window-substring

# 0.  투 포인터와 슬라이딩 윈도우
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = collections.Counter(t)
        missing = len(t)
        l = start = end = 0  # start와 end는 정답

        for r, ch in enumerate(s, 1) :
            missing -= need[ch] > 0
            need[ch] -= 1
            if missing == 0 :
                while l < r and need[s[l]] < 0 : 
                    need[s[l]] += 1
                    l += 1
                if not end or (r-l) <= (end - start) :
                    start, end = l, r
                    need[s[l]] += 1
                    missing += 1
                    l += 1
        return s[start:end]


