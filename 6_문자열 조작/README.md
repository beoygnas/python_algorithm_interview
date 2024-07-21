# 6. 문자열 조작

## 문제

### 1. 문자열 슬라이싱은 내부적으로 매우 빠르게 동작.

- 슬라이싱 > reverse() > reversed() + join() > for > while > 재귀

```python
a[start : end : step]
s[:] # list의 copy를 return, (참조x 값 복사
s[::1] # list copy, 기본값으로 동일함.
s[::-1] # step을 -1로 처리하면, 역순
s[::2] # 0, 2, 4 .. 인덱스를 가져옴.
```
