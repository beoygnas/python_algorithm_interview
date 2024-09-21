# https://leetcode.com/problems/valid-anagram
import collections

# 0. 두 글자를 정렬하면 O(nlogn)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# 0-1. Counter로 하면 O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 두 글자를 정렬하면 O(nlogn)
        # Counter로 하면 O(n)
        s_counter = collections.Counter(s)
        for ch in t : 
            if s_counter[ch] == 0 : return False
            s_counter[ch] -= 1
        
        for ch in s_counter : 
            if s_counter[ch] != 0 : return False

        return True


