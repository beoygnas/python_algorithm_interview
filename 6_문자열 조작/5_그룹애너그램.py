# https://leetcode.com/problems/group-anagrams/
# Set
import collections
from typing import * 

# 0. 내가 푼 풀이
# Counter를 이용하여 multiset으로 anagram 저장.
# anagram을 정렬 후 tuple로 처리.
# 그러다보니 시간복잡도가 최악
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = collections.defaultdict(list)
        for word in strs : 
            anagram = collections.Counter(word)
            anagram = [(k, v) for k, v in anagram.items()]
            anagram.sort(key = lambda x : (x[1], x[0]))
            anagram = tuple(anagram)
            anagram_dict[anagram].append(word)

        answer = []
        for k,v in anagram_dict.items() : 
            answer.append(v)

        return answer


