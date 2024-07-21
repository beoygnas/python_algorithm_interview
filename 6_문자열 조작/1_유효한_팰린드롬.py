# 내가 푼 풀이, 리스트 function 이용
# 시간복잡도 O(n)
class Solution :
    def isPalindrome(self, s: str) -> bool:        
        s = [ch for ch in s if ch.isalnum()]

        if s == list(reversed(s)) : 
            return True
        else : False

# 1. 리스트, pop(0), pop()
# 시간복잡도 O(n^2)
class Solution :
    def isPalindrome(self, s: str) -> bool:        
        s = [ch.lower() for ch in s if ch.isalnum()]
        
        while len(s) > 1:
            if s.pop(0) != s.pop() :
                return False

        return True
    

## 2. deque
## popleft가 O(1)이 되어 시간복잡도 O(n)
class Solution :
    def isPalindrome(self, s: str) -> bool:      
        import collections
        s = [ch.lower() for ch in s if ch.isalnum()]
        s = collections.deqeue(s)
        while len(s) > 1:
            if s.popleft() != s.pop() :
                return False

        return True
    
## 3. slicing 을 통해 reverse
## slicing은 내부코드가 C로 구성되어 있어, 훨씬 더 빠른 속도로 가능.
class Solution :
    def isPalindrome(self, s: str) -> bool:      
        import collections
        import re
        s = re.sub("[^A-Za-z0-9]", "", s).lower()
        return s == s[::-1]