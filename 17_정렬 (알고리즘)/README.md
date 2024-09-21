# 17. 정렬

### 버블정렬 (Buuble Sort)

- O(n^2)
  ```python
  def bubblesort(A) :
      for _ in range(1, len(A)) :
          for i in range(0, len(A) - 1) :
              if A[i] > A[i+1] :
                  A[i], A[i+1] = A[i+1], A[i]
  ```

### 병합정렬 (Merge Sort)

- 분할정보의 진수를 보여주는 알고리즘이며, 최선과 최악 모두 `O(nlogn)`
- 퀵정렬보다는 대부분 느리지만, 일정한 실행 속도와 stable sort이기 때문에

### 퀵정렬 (Quick Sort)

- 최선 : `O(nlong)` / 최악 : `O(n^2)` (이미 정렬된 경우)
- 분할정복, pivot을 정하고 작으면 왼쪽, 크면 오른쪽으로 파티셔닝하면서 쪼개 나가는 방식.
- partition을 수행하는데 `n`, 분할 시 최악의 경우 `n`이 될 수 있음.

```python
def quicksort(A, lo, hi) :
    def partition(lo, hi) :
        pivot, left = A[hi], lo
        for right in range(lo, hi) :
            if A[right] < pivot :
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]
        return left

    pivot = partition(lo, hi)
    quicksort(A, lo, pivot - 1)
    quicksort(A, pivot + 1, hi)
```

## 문제

58. 리스트 정렬 : https://leetcode.com/problems/sort-list
59. 구간 병합 : https://leetcode.com/problems/merge-intervals
60. 삽입 정렬 리스트 : https://leetcode.com/problems/insertion-sort-list
61. 가장 큰 수 : https://leetcode.com/problems/largest-number
62. 유효한 애너그램 : https://leetcode.com/problems/valid-anagram
63. 색 정렬 : https://leetcode.com/problems/sort-colors

## 기록

### 1. key를 통한 정렬

- comparable 객체가 아닌 경우, `lambda`를 통해 정렬
- 내림차순 정렬을 원하는 경우는, `-`를 붙인다.
  ```python
  li = [[1, 1], [2,2], [2, 3], [3,3]]
  sorted_li = sorted(li, key=lambda x: (x[0], -x[1]))
  ```

### 2. key에서 comparison에 대한 함수 변경

- compare function을 바꾸고 싶을 경우, `functools` 라이브러리의 `cmp_to_key`를 사용
- compare function의 return 값은 `1, 0, -1` 만 가능.
  - 1 : x < y, x가 y 앞으로 정렬
  - 0 : x = y, 순서가 바뀌지 않음.
  - -1 : x > y, y가 x 앞으로 정렬
    ```python
    def cmp(x1, x2) -> bool :
        if x1+x2 < x2+x1 :
            return 1
        else :
            return -1
    nums = sorted(nums, key = cmp_to_key(cmp))
    ```
