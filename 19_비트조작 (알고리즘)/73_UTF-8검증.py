# https://leetcode.com/problems/utf-8-validation

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        MASK = 0xFF
        
        state = 0
        for d in data : 
            byte = bin(d & MASK)[2:]
            print(byte)
            if state : 
                if len(byte) < 8 or not byte.startswith('10'):
                    return False
                state -= 1
            else : 
                if len(byte) < 8 :
                    continue
                elif byte.startswith('110') :
                    state = 1
                elif byte.startswith('1110') :
                    state = 2
                elif byte.startswith('11110') :
                    state = 3
                else :
                    return False
        
        if state : 
            return False    
        
        return True
                    



