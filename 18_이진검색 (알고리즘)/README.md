# 18. 이진검색

시간복잡도가 O(log n)인 대표적인 로그 시간 알고리즘, 이진탐색트리 (BST)와 유사한 점이 많다.

- Binary Search Tree: 정렬된 구조를 저장하고 탐색하는 자료구조
- Binary Search : 정렬된 배열에서 값을 찾는 알고리즘 자체

## 문제

65. 이진 검색 : https://leetcode.com/problems/binary-search
66. 회전 정렬된 배열 검색 : https://leetcode.com/problems/search-in-rotated-sorted-array
67. 두 배열의 교집합 : https://leetcode.com/problems/intersection-of-two-arrays/

## 기록

### 1. bisect 모듈

- `bisect` 모듈을 이용, 정렬을 유지한채로 들어갈 수 자리를 찾기 때문에 `return index`의 값과 해당 위치의 값을 확인해야 한다.

  ```python
  index = bisect.bisect_left(nums, target)

  if index < len(nums) and nums[index] == target :
      return index
  else :
      return -1
  ```

### 2. overflow를 고려한 mid 설정

- python은 임의 정밀도 정수형를 사용하기 때문에, overflow를 고려하지 않아도 된다. 하지만 C언어 같은 경우, `mid` 의 계산에서 overflow가 발생할 수 있다.
- 뺄셈을 하고, 그 차를 반으로 다눈 후 낮은 수에 더하는 방법을 채용하면 이를 방지할 수 있다.

```python

mid = (left + right) // 2
mid = left + (right - left)//2
```
