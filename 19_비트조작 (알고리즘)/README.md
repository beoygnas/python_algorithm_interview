# 19. 비트조작

### 부울 연산자

- 기본연산자 : `and`, `or`, `not`
  ```python
  True and False
  True or False
  not True
  ```
- 기본연산자로 보조연산 `XOR`을 구성할 수 있음.
  ```python
  x=y=True
  (x and not y) or (not x and y) # False
  ```

### 비트연산자

- 기본연산자
  ```python
  True & False # False
  True | False # True
  True ^ True  # False (xor 연산)
  ~ True       # 2 (비트로 not, 뒤집기)
  ```
- 비트연산자 NOT (`~`) 은 (2의 보수 - 1) 처리를 해줘서 2가 됨.

### 비트 조작 퀴즈

- 뒤집고 xor 연산하기?
  ```python
  bin(0b0101 ^ ~0b1100)
  # ~0b1100 = 0b1111..0011 not 처리 : 전부뒤집기
  # 0b0101 ^ 0b1111..0011 = 0b1111..0110
  # -(0b0000..1001 + 1), 2의보수처리 : 뒤집고 + 1
  >> -0b1010
  ```

### 자릿수 제한 비트연산

- 위에 처럼 not연산을 막쓰면, 자릿수로 인해 잘못된 결과가 나올 수 있다.
- 다음과 같이 MASK를 통해 자릿수 제한이 필요한 경우가 있다.
  ```python
  MASK = 0b1111 # 0b1100의 자릿수를 제한한 후의 not연산 효과를 줌)
  bin(0b0101 ^ (0b1100 ^ MASK))
  # bin(0b0101 ^ 0b11)
  # bin(0b110)
  > 0b110
  ```

### 2의 보수

- 음수를 표현하기 위한 숫자 포맷
  - `0b0010 = -0b1110` (`6 = -(-6)`)
- 어떤 수의 2의 보수 표현을 얻기 위해서는, `MASK`와 `&`연산을 통해 얻는다.
  - 파이썬은 정수를 보통 28비트로 저장하는데, 4비트 체제에서 2의보수를 표현하기 위해서는 `MASK`를 통한 자릿수 제한이 필요하다.

```python
MASK = 0xF     # 0b1111
bin(7 & MASK)  # 0b0111
bin(-8 & MASK) # 0b1000
```

### 2의 보수 연산과 비트연산자 NOT

- 2의 보수 연산 = `비트연산 NOT (flip) + 1`
- 비트연산 NOT = `2의 보수 연산` 이후 - 1

## 문제

## 기록

70. 싱글 넘버 : https://leetcode.com/problems/single-number
71. 해밍 거리 : https://leetcode.com/problems/hamming-distance
72. 두 정수의 합 : https://leetcode.com/problems/sum-of-two-integers
73. UTF-8 검증 : https://leetcode.com/problems/utf-8-validation
74. 1비트의 개수 : https://leetcode.com/problems/number-of-1-bits

### 1. 파이썬의 진법 표현

```python
bin() # 2진수 변환, return str
int() # 10진수 변환
hex() # 16진수 변환, return str
```
