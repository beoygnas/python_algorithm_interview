# 10. 데크, 우선순위 큐

- 데크 : 스택과 큐의 연산을 모두 갖고 있는 복합자료형
- 우선순위 큐 : 추출 순서가 일정하게 정해져 있지 않은 큐

### 데크

- `Double-Ended Queue`, 양쪽 끝을 모두 O(1)에 추출할 수 있는, 큐를 일반화한 형태의 추상자료형 (ADT)
- 배열로도 원형큐와 같이 구현이 가능하지만, 이중연결리스트로 구현하는 것이 잘 어울림.
  - See [26\_원형데크디자인.py](26_원형데크디자인.py)

### 우선순위 큐

- 특정 조건에 따라 우선순위가 가장 높은 요소가 추출되는 자료형.
- 최단경로 알고리즘, Heap 자료구조와 관련이 깊다.

## 문제

26. 원형데크디자인 : https://leetcode.com/problems/design-circular-deque
27. k개 정렬 리스트 병합 : https://leetcode.com/problems/merge-k-sorted-lists

## 기록

### 1. `heapq`

- 파이썬에서 우선순위 큐 풀이에 대부분 사용되는 모듈

```python
heapq.heappush(queue, item) # item tuple의 인자 순서대로 min heap push
heapq.heapop(queue)
```

- `PriorityQueue` vs `headpq`
  - `PriorityQueue`도 내부적으로 `headpq` 로 구현되있지만, thread safe를 보장한다.
  - python은 GIL로 인해 multi threading이 제한되어, 사실상 유명무실한 차이이며 대부분 구현에서도 `heapq`모듈을 사용한다.
