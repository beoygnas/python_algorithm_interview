# 5. 리스트, 딕셔너리

## List

- Mutable List, 입력순서가 유지되며 동적배열로 구성되어 있다.
- 연산 별 시간복잡도
  | 연산 | 시간복잡도|  
  | ------- | ------- |
  | `len(a)` | `O(1)` |
  | `a[i]` | `O(1)` |
  | `a[i:j]` | `O(k)` |
  | `k in a` | `O(n)` |
  | `a.count(k)` | `O(n)` |
  | `a.index(k)` | `O(n)` |
  | `a.append(k)` | `O(1)` |
  | `a.pop()` | `O(1)` |
  | `a.pop(0)` | `O(n)`, dequeue 을 사용하여 `O(1)`|
  | `del a[i]` | `O(n)` |
  | `a.sort()` | `O(nlogn)` |
  | `min(a), max(a)` | `O(n)` |
  | `a.reverse()` | `O(n)` |

### List 특징

- Cpython에서는, element에 대한 **pointer 목록**을 갖고 있는 구조체 (`Struct`)로 구현되어 있다.
  - 이로 인해, list의 element들이 각기 다른 자료형일 수 있어 편리하다.
  - 각기 다른 자료형은 차지하는 크기가 다르므로, 연속적인 메모리 공간에 할당할 수는 없다.
  - index 조회 시(`a[k:k+3]`) 에도, 모든 포인터의 위치를 찾아가서 타입코드 및 value를 확인해야하므로 속도적인 면에서 trade-off가 발생.

## Dictionary

- key / value 구조로 이루어진 dictionary는 내부적으로 `hash table`로 구현되어 있다.
- `hashing` : num, str, set 등의 immutable object를 `key`로 사용할 수 있다.
  - 입력과 조회 모두 `O(1)`
  - 최악의 경우 `O(n)`이 되지만, Amortized Analysis에 따른 시간복잡도는 O(1)이다.
- hash table의 연산 별 시간복잡도
  | 연산 | 시간복잡도|  
   | ------- | ------- |
  | `len(a)` | `O(1)` |
  | `a[key]` | `O(1)` |
  | `a[key] = value` | `O(1)` |
  | `key in a` | `O(1)` |

- value의 입력순서는 `collections.OrderedDict()` 를 사용해야 하며 (<python3.6), 일반적으로 지원해주지 않는다.

### dictionary 활용방법

```python
a = {} # dictionary 선언

if key in a : # key 존재 여부 확인.

for k,v in a.items() : # key, value 동시 순회

del a[key] # key 삭제
```

### dictionary module

- See [dict.ipynb](./dict.ipynb)

1. defaultdict

   ```python
   a = collections.defaultdict(int)
   a['A'] = 5
   a['C'] += 1 # default int인 0을 가지는 key C를 생성해서 1이 저장됨.
   a # defaultdict(int, {'a': 5, 'c': 1})
   ```

2. Counter

   ```python
   a = [1,2,3,4,5,5,5,6,6]
   b = colletcions.default
   b # Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 3, 6: 2})
   b.most_common(1) # [(5, 3)]
   ```

3. OrderedDict

   - 순서가 유지됨

   ```python
   python
   a = collections.OrderedDict()
   a['key1'] = 1
   a['key2'] = 2
   a['key4'] = 4
   for k,v in a.items() :
       print(k, v)
   ```
