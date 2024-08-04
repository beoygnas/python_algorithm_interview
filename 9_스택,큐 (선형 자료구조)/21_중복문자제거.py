# https://leetcode.com/problems/remove-duplicate-letters
import collections


# 1. 재귀 풀이
# 백트래킹? 사전순서대로 모든 경우의수를 확인한다.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        for ch in sorted(set(s)) : 
            suffix = s[s.index(ch):]
            if set(s) == set(suffix) : 
                return ch + self.removeDuplicateLetters(suffix.replace(ch, ''))

        return ''


# 2. 스택 + collections을 이용한 풀이.
# 원래 접근을, stack으로 했는데, 뒤에 나올 alpha에 대한 정보를 어디서 구할지 찾지 못해 못풀었음.
# 그걸 counter로 해결
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []
    
        for ch in s : 
            counter[ch] -= 1
            if ch in stack : continue
            while stack and ch < stack[-1] and counter[stack[-1]] > 0 :
                stack.pop()

            stack.append(ch)
        
        return ''.join(stack)
    
# in_stack 을 이용하여, stack 안에 있는지 체크할 때의 시간복잡도를 줄인다.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, in_stack, stack = collections.Counter(s), collections.defaultdict(int), []

        for ch in s : 
            counter[ch] -= 1
            if in_stack[ch] == 1 : continue

            while stack and ch < stack[-1] and counter[stack[-1]] > 0 :
                in_stack[stack.pop()] = 0

            stack.append(ch)
            in_stack[ch] = 1
            
        return ''.join(stack)