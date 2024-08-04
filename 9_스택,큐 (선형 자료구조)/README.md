# 9. 스택, 큐

- 스택 : `LIFO` (Last in First Out)
- 큐 : `FIFO` (First in First Out)
- 파이썬에서는 스택과 큐에 대해 따로 자료형이 있지않고, `list` 와 `deque`에서 각각의 모든 연산을 지원.
  - `list`는 동적배열로 이루어져 있어, 큐의 연산을 수행하기에는 효율적이지 않음.

### Stack

- push, pop 두가지 연산을 지원하는 추상자료형 (ADT)
- [연결리스트로서의 구현](stack_linked_list.ipynb)

### Queue

- 추가 예정

## 문제

20. 유효한 괄호 : https://leetcode.com/problems/valid-parentheses
21. 중복 문자 제거 : https://leetcode.com/problems/remove-duplicate-letters (어려움)

## 기록

### 1. `list`의 emtpy check

```python
stack = []
if stack :  # empty check
    pritnt("stack is not empty")
```
