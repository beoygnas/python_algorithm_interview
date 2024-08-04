# https://leetcode.com/problems/implement-stack-using-queues/description/
import collections
from typing import * 

# 0. 두 개의 큐를 이용한 구현
# top, pop이 필요할때 한쪽 큐에 옮겨놓는다. -> 시간복잡도는 O(n) (stack에서는 O(1))
# push 는 O(1)
class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        self.tmp_q = collections.deque()
        while self.q :
            self.tmp_q.append(self.q.popleft())
        while len(self.tmp_q) > 1 :
            self.q.append(self.tmp_q.popleft())
        return self.tmp_q.popleft()
        

    def top(self) -> int:
        self.tmp_q = collections.deque()
        front = None
        while self.q :
            self.tmp_q.append(self.q.popleft())
        while self.tmp_q :
            front = self.tmp_q.popleft()
            self.q.append(front)
        return front

    def empty(self) -> bool:
        return len(self.q) == 0


# 1. push에서 넣어줄때부터 스택처럼 넣어주기 O(n)
# 추가 메모리 공간도 필요없고, 더 간결함. len(queue) - 1로 방금 넣어준건 제외하고 하는게 생명   
class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1) :
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()
        
    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0