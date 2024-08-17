# 12. 그래프

- 그래프이론에서 그래프란, 객체의 일부 pair들이 연관되어 있는 객체 집합 구조.

### 오일러 경로

- 모든 vertex가 짝수 개의 degree를 갖는다면, 모든 edge를 한번씩만 방문하며 모든 vertex를 방문할 수 있다.
- 오일러 경로 : 모든 간선을 한 번씩 방문하는 유한 그래프

### 해밀턴 경로

- 오일러 경로가 `edge`를 기준으로 한다면, 해밀턴 경로는 `vertex`를 기준으로 함, 모든 정점을 한 번씩 방문하는 그래프.
- `traveling salesman problem` : 모든 정점을 지나고 원래의 출발점으로 돌아오는 경로중, 최단 경로 찾기문제.
  - 최단거리 해밀턴 cycle 찾기 문제, NPC
  - brute force : `n!` / dp : `(n^2)*(2^n)!`

### 그래프 순회

- 그래프 탐색이라고도 불리며, 그래프의 각 정점을 방문하는 과정을 말함.
- See [graph_traversal.ipynb](./graph_traversal.ipynb)
- `DFS` : 보통 스택, 재귀로 구현, 백트래킹
- `BFS`: 큐로 구현, 최단거리

### 백트래킹

- solution에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 그 후보를 포기(`Backtrack`) 하여 정답을 찾아가는 범용적인 알고리즘
- 제약 충족 문제 (Constraint Satisfaction Problems)에 유용함.
- ex) 트리의 `pruning`

### 제약 충족 문제

- 수많은 constraints을 충족하는 상태(states)를 찾아내는 수학문제
- ex) 스도쿠, 4색문제, 배낭문제, 문자열 파싱 등등

## 문제

32. 섬의 개수: https://leetcode.com/problems/number-of-islands
33. 전화 번호 문자 조합: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
34. 순열: https://leetcode.com/problems/permutations
35. 조합: https://leetcode.com/problems/combinations
36. 조합의 합: https://leetcode.com/problems/combination-sum
37. 부분 집합: https://leetcode.com/problems/subsets
38. 일정재구성: https://leetcode.com/problems/reconstruct-itinerary

## 기록

### 1. 0으로 초기화된 2차원 배열 생성

```python
# m개의 배열이 같은 object(list)를 가리키게 되어, 초기화 및 객체 접근 시 문제 발생
[[0] * n] * m

# m개의 리스트를 하나하나 다른 객체를 생성해줌.
[[0] * n for _ in range(m)]
```

### 2. itertools를 이용한 순열/조합

- [`itertools.ipynb`](./itertools.ipynb)

```python
a = ['a', 'b', 'c']
list(itertools.permutations(a)) # 순열
list(itertools.combinations(a, 2)) # 조합
```

### 3. 객체 복사

- python에서 변수의 값을 할당하는 모든 행위는, value 객체에 대한 참조를 바꿔주는 것을 의미.
  - 변수의 할당된 값을 바꿔줄 때 mutable 객체라면, 의도치 않게 그 객체를 가르키고 있는 다른 변수의 값을 바꿀 수도 있음.
  - 따라서 **값만 똑같은 새로운 객체**를 할당하고 싶을 때는, `copy()` 같은 메소드를 사용한다.

```python
a = [1,2,3]
b = a
c = a[:]
d = copy(a)
id(a), id(b), id(c), id(d) # a=b != c != d
```

- 또한, 객체가 `nested list` 와 같이 복잡할 경우에는 모든 element에 대해서 copy()가 이루어질 수 있도록 `deepcopy()`를 사용한다.

### 4. list + list 연산

- list + list는, 리스트를 append 한 새로운 list 객체를 return

```python
elements.append(candidates[i])
fun(elements, i, sum+candidates[i])
elements.pop()
```

```python
fun(elements + [candidates[i]], i, sum+candidates[i])
```
