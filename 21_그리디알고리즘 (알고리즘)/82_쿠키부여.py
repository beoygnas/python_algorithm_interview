# https://leetcode.com/problems/assign-cookies

# 0. greed factor가 적은애부터, 투포인터로 매칭시켜주면 될듯
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = j = answer = 0
        g.sort()
        s.sort()
        
        while i < len(g) and j < len(s) :
            if g[i] <= s[j] :
                answer += 1
                i += 1 
                j += 1
            else : 
                j += 1
        
        return answer

# 1. 최적화
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = j = 0
        g.sort()
        s.sort()
        
        while i < len(g) and j < len(s) :
            if g[i] <= s[j] :
                i += 1 
            j += 1
        
        return i
