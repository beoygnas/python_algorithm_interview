# https://leetcode.com/problems/implement-queue-using-stacks/
import collections
from typing import * 

# 1. 스택 두개를 이용.
# 언제나 한쪽스택에 몰아놔야하는 건 아니다. 최악은 O(n) 이겠지만, 분할 상환 분석에 의해 O(1) 정도로 봄.
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)
    
    def pop(self) -> int:
        self.peek() # 뒤집고,
        return self.output.pop() # pop

    def peek(self) -> int:
        if not self.output : 
            while self.input : 
                self.output.append(self.input.pop())    
        return self.output[-1]

    def empty(self) -> bool:    
        return len(self.stack) == 0


