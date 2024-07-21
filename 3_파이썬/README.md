# 파이썬

## 파이썬 문법

- Interpreter / Version : Cpython / python 3.7
- Indent : 4
- Naming Convention : snake_case
- Type Hint : 권장

### List Comprehension

- 파이썬의 대표적 특징. 가독성을 위해 `list comprehension` 사용을 권장 (람다표현식이나 map,filter와 같은 함수형 기능 대신)
- 리스트 뿐만 아니라, dict에서도 사용이 가능

  ```python
  # list
  [n*2 for n in range(1, 10+1) if n%2 == 1]

  # dict
  {k:v for k, v in some_dict.items()}
  ```

### Generator

- 반복문의 iteration 동작을 제어할 수 있는 루틴형태
- `iterator`를 생성하고, `yield`를 포함. `next()`를 통해 다음 값을 생성.
- 반복문의 메모리 효율성, 성능 및 코드 재활용성을 위해 사용.

  ```python
  def get_natural_number():
      n = 0
      while True :
          n+=1
          yield n

  generator = get_natural_number()
  for _ in range(100):
      print(next(generator))
  ```

### range

- `range()`를 for문에서 사용할 경우 `generator` 방식을 활용하여, 내부적으로 `next()`를 통해 다음 숫자를 생성.
- list와 동일하게 사용이 가능하지만, generator를 통해 훨씬 메모리 사용량이 적음.
- see [generator.ipynb](generator.ipynb)

### enumerate

- `list`, `set`, `tuple` 등을 `index`를 포함한 `enumerate` 객체로 리턴.
- enumerate의 각 개체는 `tuple`

  ```python
  a = [1,2,3,4]
  list(enumerate(a))

  > [(0, 1), (1, 2), (2, 3), (3, 4)]
  ```

### 나눗셈

```python
5/3           # 1.666667  return float class
5//3          # 1         return int = int(5/3)
5%3           # 2         return int
divmod(5, 3)  # (1, 2)    return (int, int)
```
