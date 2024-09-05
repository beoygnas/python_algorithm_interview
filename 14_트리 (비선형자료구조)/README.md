# 14. 트리

- 정의 (그래프 이론) : cycle이 없는, 무방향 그래프 (자료구조에서는 단방향 자식->노드)
- 루트 값과, 부모-자식 관계의 서브트리로 구성되며, 서로 연결된 노드의 집합
- 재귀로 정의된(recursively defined) + 자기참조 (self-referential) 자료구조]
  - 루트도 트리고, 자식도 트리고, 또 그 자식도 트리다.
- A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

### 트리의 각 명칭

- 트리는 항상 root부터 시작.
  - 루트는 자식 노드와 간선으로 연결되며, 부모 -> 자식의 **단방향**만으로 구성
- 차수(degree) : 자식 노드의 개수
- 크기(size) : 자신을 포함한 모든 자식 노드의 개수
  - height : 루트부터 leaf 까지 거리
  - depth : 루트에서 현재 노드까지 거리

### 그래프 vs 트리

- 트리는 순환 구조를 갖지 않는 방향그래프이다.
  - 트리는 부모 노드 -> 자식 노드의 단뱡향 / 그래프는 양방향
- 트리는 하나 이하의 부모 노드만을 가져야 하며, 루트는 하나만 존재해야 함.
  - n개의 노드가 있다면, 간선은 n-1개가 존재
- 레벨, 계층의 개념 또한 큰 차이라고 할 수 있다.

### 이진 트리

- binary tree : 모든 노드의 degree가 2 이하인 트리
  - 간결하여 대체로 트리는 대부분 이진 트리를 일컫음.
- 이진트리는 다음과 같은 종류로 나뉜다.
  1. full binary tree : 모든 노드가 0 또는 2개의 자식 노드를 가지는 이진트리
  2. complete binary tree : 마지막 level을 제외하고는 full binary 트리이며, 마지막 레벨의 모든 노드는 왼쪽부터 채워진 이진 트리
  3. perfact binary tree : 리프를 제외한 모든 노드가 2개의 자식 노드를 가지며, 모든 리프 노드는 동일한 depth, level을 갖는다.

### 이진 탐색 트리 (BST)

- 노드의 왼쪽 서브트리에는 그 노드의 값보다 작은 값이, 오른쪽 서브트리에는 같거나 큰 값들을 지닌 노드들로 이루어져 있는 **정렬된 트리**

  - pros : 시간복잡도가 `O(log n)`
  - cons : 균형이 제대로 이루어지지 있자 않다면, `O(n)`

- **자가 균형 이진 탐색 트리 (self-balancing binary search tree)**
  - 삽입, 삭제 시 자동으로 높이를 작게 유지하는 노드 기반의 이진 탐색 트리다.
  - 최악의 경우에도 이진 트리의 균형이 잘 맞도록 유지한다.
  - ex) `AVL트리`, `레드-블랙 트리`

## 문제

42. 이진 트리의 최대 깊이 (https://leetcode.com/problems/maximum-depth-of-binary-tree)
43. 이진 트리의 직경 (https://leetcode.com/problems/diameter-of-binary-tree)
44. 가장 긴 동일 값의 경로 (https://leetcode.com/problems/longest-univalue-path)
45. 이진 트리 반전 (https://leetcode.com/problems/invert-binary-tree)
46. 두 이진 트리 병합 (https://leetcode.com/problems/merge-two-binary-trees)
47. 이진 트리 직렬화 & 역직렬화 (https://leetcode.com/problems/serialize-and-deserialize-binary-tree)
48. 균형 이진 트리 (https://leetcode.com/problems/balanced-binary-tree)
49. 최소 높이 트리 (https://leetcode.com/problems/minimum-height-trees)
50. 정렬된 배열의 이진 탐색 트리 변환 (https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree)

## 기록

### 1. nested function에서 class variable를 사용하는 이유

- 다음과 같이 class 변수로 사용하지 않고 부모함수의 변수를 재할당할 경우, `dfs()` 함수 내에서 local variable로 새로 선언이 된다.

  ```python
  answer = 0
  def dfs() :
      ...
      answer = max(answer, -1)
      ...
  # UnboundLocalError: cannot access local variable 'answer' where it is not associated with a value
  ```

- `nonlocal answer` 를 사용하거나, class variable로 사용해야함. (See [43\_이진트리의직경.py](./43_이진트리의직경.py))

### 2. defaultdict에 None 넣기

- defaultdict의 default 값으로 None을 넣어줘야 할 떄 다음과 같이 lambda를 이용하여 선언

  ```python
  tree_list = collections.defaultdict(lambda: None)
  ```

### 3. list/dict 에서 값 제거하기

- `list`
  - remove(value)
  - pop(index)
  ```python
    parent = graph[leaf].pop() # pop으로 마지막 index 제거, O(1)
    graph[parent].remove(leaf) # remove + value로 제거, O(n)
  ```
- `dict`
  - del / pop : `O(n)`
  ```python
  del graph[leaf] #  삭제
  graph.pop(leaf, None) # leaf라는 키가 있으면 제거, 없으면 None
  ```
