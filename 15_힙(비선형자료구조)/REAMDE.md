# 15. 힙

아래 조건을 만족하는 트리 기반의 자료구조.

- 힙의 특성 (부모가 항상 자식보다 작거나같다 / 크거나 같다. min/max heap)
- Almost Complete Binary Tree (마지막 level을 제외하고는 full binary tree, 마지막 레벨의 모든 노드는 왼쪽부터)

`heapq` 모듈은 힙으로 구현되어있고, 파이썬은 `min heap` 만 구현됨.

- 우선순위 큐는 보통 heap으로 구현하고, 힙은 주로 배열로 구현.

### 특징

- 정렬된 구조가 아니다.
  - 부모 노드는 항상 작다는 부모-자식 간의 관계는 있지만, 좌우에 대한 관계는 정의를 하지 않음.
- 항상 균형을 유지하는 특징 때문에, 다양한 분야에 널리 활용됨.
  - 다익스트라, mst emdemd

### 힙 연산

- See [heap.ipynb](./heap.ipynb)
- 삽입 : 1) 힙의 가장 마지막에 원소 추가 (O(1))+ 2) heapify (log n)
- 추출 : 1) 힙의 첫 언소를 제거 2) 마지막원소를 루트로 두고 heapify (log n)

## 문제

55. 배열의 K번째 큰 요소 : https://leetcode.com/problems/kth-largest-element-in-an-array/

## 기록

### 1. `Binary Heap` Vs `Binary Search Tree`

- 힙은 상/하 관계를 보장 (부모/자식)
  - min/max 조회에 있어 O(1)에 가능하여, 우선순위 큐에 주로 사용
- BST에서는 좌/우 관계를 보장
  - 탐색과 삽입 모두 log(n)을 보장, 모든 값이 정렬되어야 할 때 사용.

### 2. `heapq` 모듈의 이용

- `heapq.heappush(heap, item)`
- `heapq.heappop(heap)`
- `heapq.heapify(list)` : return 타입이 None으로, list를 그냥 heap정렬함.
- `heapq.nlargest(n, nums)` : n개 까지의 큰 값을 list로 return. (큰 값부터 return)
  - `heapq.nlargest(n, nums)` : 반대의 기능을 함.
