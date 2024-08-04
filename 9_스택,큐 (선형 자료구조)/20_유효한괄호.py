# https://leetcode.com/problems/valid-parentheses

# 0. 내가 푼 풀이, map으로 좀 더 간결하게
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        p_map = {']' : '[', '}' : '{', ')' : '('} 

        for ch in s : 
            if ch not in p_map : 
                stack.append(ch)
            else: 
                if not stack or stack.pop() != p_map[ch] :
                    return False
        
        if stack : return False
        else : return True

# 1. 좀 더 간결하게 할 수 있다.
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        p_map = {']' : '[', '}' : '{', ')' : '('} 

        for ch in s : 
            if ch not in p_map : 
                stack.append(ch)
            elif not stack or stack.pop() != p_map[ch] :
                    return False
        
        return len(stack) == 0