# 6. 문자열 조작

## 문제

1. 유효한 팰린드롬 : https://leetcode.com/problems/valid-palindrome
2. 문자열 뒤집기 : https://leetcode.com/problems/reverse-string
3. 로그파일 재정렬 : https://leetcode.com/problems/reorder-data-in-log-files
4. 가장 흔한 단어 : https://leetcode.com/problems/most-common-word/
5. 그룹 애너그램 : https://leetcode.com/problems/group-anagrams/
6. 가장 긴 팰린드롬 부분 문자열 : https://leetcode.com/problems/longest-palindromic-substring/

## 기록

### 1. 문자열 슬라이싱

- 문자열 슬라이싱은 내부적으로 가장 빠르게 동작
- 슬라이싱 > reverse() > reversed() + join() > for > while > 재귀

```python
a[start : end : step]
s[:] # list의 copy를 return, (참조x 값 복사
s[::1] # list copy, 기본값으로 동일함.
s[::-1] # step을 -1로 처리하면, 역순
s[::2] # 0, 2, 4 .. 인덱스를 가져옴.
```

### 2. list `pop(0)` vs deque `popleft()`

```python
li = [1, 2, 3, 4, 5]
deq = collections.deque(li)
li.pop(0) # 시간복잡도 O(n)
deq.popleft() # 시간복잡도 O(1)
```

### 3. 람다 연산자

- [3\_로그파일\_재정렬.py](./3_로그파일_재정렬.py)

```python
letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))
# sort의 key로 람다표현식을 사용했으며,
# 두 가지 key를 통해 첫 번째 key에서 동일한 경우에 대해서도 대비.
```

### 4. 정규표현식

- 문자열에서 정규표현식을 통한 데이터 전처리는 편리하고 용이함.
- [정규표현식기초](./정규표현식기초.md), [regex.ipynb](./regex.ipynb)
- [4\_가장\_흔한\_단어.py](./4_가장_흔한_단어.py)

```python
paragraph = re.sub(r'[^a-zA-Z]', ' ',  paragraph)
paragraph = paragraph.lower().split() # 공백 제외하고 split()
words = [word for word in paragraph if word not in banned]
```

### 5. `sort()` vs `sorted()`

- [5\_그룹애너그램.py](./5_그룹애너그램.py)
- `sort()`
  - in-place sort 방식, 리스트 자체를 정렬하며 추가메모리 및 리턴값이 없음. (`None`)
- `sorted()`
  - 정렬된 새로운 리스트를 return

```python
a = [1,2,3,4, 5]
a.sort(reverse=True)
b = sorted(a, reverse=True)
```

### 6. UTF-8

- ASCII : 1byte로 문자표현 (7bit + 1bit checksum)
- Unicode : 2~4 byte로 문자표현, 영문자도 2byte로 표현하여 비효율적
- UTF-8 : 가변길이 문자 인코딩 방식, (ASCII 127까지는 완전히 동일). 시작비트를 통해, 문자가 차지하는 전체 바이트를 정할 수 있다.
- python3 부터는, 문자열이 모두 유니코드로 전환되어 한영 특수문자 모두 출력에 제약이 없다.
  - 내부적으로 `UTF-8`을 사용하지는 않고, 문열에 포함된 문자 범위에 따라 서로 다른 고정 인코딩 방식을 택하여, 문자열 슬라이싱시에 원하는 문자의 index로 쉽게 접근할 수 있도록 하.ㅁ
  - ex) 문자열에 따라 모두 ASCII 처리가 가능하면 `Latin-1` 인코딩 (고정 1바이트 인코딩)을 사용하고, 대부분의 경우 UCS-2 (고정 2바이트 인코딩), 특수문자가 포함된 경우 USC-4(고정 4바이트 인코딩)으로
