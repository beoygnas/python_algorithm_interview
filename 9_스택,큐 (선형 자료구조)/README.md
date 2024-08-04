# 9. 스택, 큐

- 스택 : `LIFO` (Last in First Out)
- 큐 : `FIFO` (First in First Out)
- 파이썬에서는 스택과 큐에 대해 따로 자료형이 있지않고, `list` 와 `deque`에서 각각의 모든 연산을 지원.
  - `list`는 동적배열로 이루어져 있어, 큐의 연산을 수행하기에는 효율적이지 않음.

### Stack

- push, pop 두가지 연산을 지원하는 추상자료형 (ADT)
- [연결리스트로서의 구현](stack_linked_list.ipynb)

### Queue

- 시퀀스의 end에는 entity를 추가하고 front 에서는 제거할 수 있는 엔티티 컬렉션.
- [큐를 이용한 스택 구현](23_큐를이용한스택구현.py)
- [스택을 이용한 큐 구현](24_스택을이용한큐구현.py)

## 문제

20. 유효한 괄호 : https://leetcode.com/problems/valid-parentheses
21. 중복 문자 제거 : https://leetcode.com/problems/remove-duplicate-letters (어려움)
22. 일일 온도 : https://leetcode.com/problems/daily-temperatures
23. 큐를 이용한 스택 구현 : https://leetcode.com/problems/implement-stack-using-queues/
24. 스택을 이용한 큐 구현 : https://leetcode.com/problems/implement-queue-using-stacks/
25. 원형 큐 디자인 : https://leetcode.com/problems/design-circular-queue

## 기록

### 1. `list`의 emtpy check

```python
stack = []
if stack :  # empty check
    pritnt("stack is not empty")
```

### 2. 0으로 초기화된 list 만들기

- C++의 전역변수 배열은 0으로 초기화 됨.
- 비슷하게 파이썬에서 0으로 초기화된 리스트 만들기

```python
length = 10
zero_list = [0] * length
```

### 3. Circular Queue

- 기존의 큐는, 큐의 공간이 꽉찰 경우에 deQueue로 인해 앞에 공간이 남음에도 불구하고 element를 추가할 수 없다.
  - 동적 배열을 사용한 큐에서는 배열의 가장 앞에서부터 데이터를 꺼내오기 때문에, 데이터를 꺼낸 후 그 다음 인덱스의 데이터들을 모두 한 칸씩 이동시켜줘야 한다는 문제가 있다. (dequeue가 O(n)이 됨)
- 앞의 공간을 재활용할 수 있다는 장점이 있다.
- 투 포인터와 비슷하게 구현이 가능. See [25\_원형큐디자인.py](25_원형큐디자인.py)
