# 7. 배열

- 자료구조는 크게

  1. 메모리 공간 기반의 `contiguous` 방식 (`array`)
  2. 포인터 기반의 `link` 방식 (`linked list`)

  으로 나뉘며 기본이 된다. (ex. ADT를 구현할 때 주로 stack은 linked list로, 큐는 array로 구현한다. 반대도 가능)

- 배열은, 연속된 메모리 공간에 할당이 되며, 어느 위치에서나 `O(1)`에 조회가 가능.

### 동적배열

- 배열은 고정된 크기만큼의 연속된 메모리 할당인데, 고정된 크기를 가늠하기 힘들때가 많다.
  - 미리 크기를 지정하지 않고, 자동으로 조정할 수 있다면?
- 파이썬(동적 프로그래밍 언어의 대표)의 `list`는 동적배열을 지원하며, 따로 정적배열은 지원하지 않는다.
- 원리 : 초기값을 작게 잡고, 꽉 채워지게 되면 `doubling` 등의 방법으로 배열의 크기를 증가시킨다.
  - 당연히 크기를 증가시키는 과정에서 시간적 overhead가 있지만, 치명적이고 자주 발생하는 상황은 아님.

## 문제

7. 두 수의 합 : https://leetcode.com/problems/two-sum/
8. 빗물트래핑 : https://leetcode.com/problems/trapping-rain-water/
9. 세 수의 합 : https://leetcode.com/problems/3sum/
10. 배열파티션1 : https://leetcode.com/problems/array-partition/
11. 자신을 제외한 배열의 곱 : https://leetcode.com/problems/product-of-array-except-self/
12. 주식을 사고팔기 가장 좋은 시점 : # https://leetcode.com/problems/best-time-to-buy-and-sell-stock

## 기록

### 1. `list.index(value)`

- 원하는 value의 첫번째 index 찾기.
- list는 `find()`가 없다. string에는 있음.

### 2. dict에 key가 있는지 조사.

- `key in dict{}` 하는게 가장 간단하다.
- `key in dict.values()` -> 끔찍한 방식

### 3. 투포인터

- 명확하게 정의된 것은 없지만, 주로 **정렬된 배열**을 대상으로 함.

### 4. 중복되는 것을 배제하여 시간 단축

- [9\_세수의합.py](./9_세수의합.py)

### 5. 빈 배열 check

```python
li = []
if not lis : # 비었을 떄
else : # 안비었을 때
```
