# 6. 문자열 조작

## 문제

1. 유효한 팰린드롬 : https://leetcode.com/problems/valid-palindrome
2. 문자열 뒤집기 : https://leetcode.com/problems/reverse-string
3. 로그파일 재정렬 : https://leetcode.com/problems/reorder-data-in-log-files
4. 가장 흔한 단어 : https://leetcode.com/problems/most-common-word/

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
