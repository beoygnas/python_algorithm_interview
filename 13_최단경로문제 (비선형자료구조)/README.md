# 13. 최단 경로 문제

- 각 간선의 가중치 합이 최소가 되는 두 정점 사이의 경로를 찾는 문제이다.

### 다익스트라 알고리즘

- 노드 주변의 최단 경로만을 택하는 대표적인 그리디 알고리즘
- 탐색시에는 BFS를 이용
- 최초 구현은 `O(V^2)`, 우선순위큐를 적용하면 O(E log V)에 가능.

## 문제

40. 네트워크 딜레이 타임 (https://leetcode.com/problems/network-delay-time)

## 기록

### 1. heapq 모듈

- 기본적으로 minheap, 따로 maxheap을 제공하지는 않아서 음수를 붙이는 방식으로 함.
- items가 tuple일 경우, tuple 순서대로 오름차순으로 `min_heap`이며, 각 element는 < 연산이 가능해야 함

```python
import heapq
heap = []
heapq.heappush(heap, items)
heapq.heappop(heap)
```
