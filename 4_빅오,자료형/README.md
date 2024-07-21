# 빅오, 자료형

## 빅오 표기법

- 입력값이 무한대로 향할때, 함수의 상한을 설명하는 수학적 표기 방법
- 시간복잡도 : 어떤 알고리즘을 수행하는데 걸리는 시간을 설명하는 계산 복잡도
- 시간복잡도와 공간복잡도는 trade-off 관계

## 자료형

### 숫자

- See [number.ipynb](number.ipynb)

#### int

- 파이썬에서는 정수 숫자 자료형으로 int만을 제공.
- C와 다르게, Arbitrary-precision 정수형으로, 숫자가 커지면 4byte씩 메모리 추가 할당.
  - 정수를 숫자의 배열로 간주하여, 무제한 자릿수를 제공.

#### bool

- 내부적으로 1(true), 0(false)의 int 서브클래스

### 매핑

- key와 value로 구성된 복합 자료형, python에서는 `dict`를 기본으로 제공

### 집합

- 중복된 값을 갖지 않는 자료형
- 입력 순서가 유지되지 않으며, 중복된 값은 하나만 유지

```python
a = set()
b = a = {'a', 'b', 'c'}
set()
```

### 시퀀스

- 특정 대상의 순서 있는 나열 (string : char의 순서 있는 나열)
- python에서는 list가 사실상 배열의 역할을 함.
- See [sequence.ipynb](sequence.ipynb)

#### imutable

- 값을 변경할 수 없음.
- str, tuple, bytes

#### mutable

- 값을 변경할 수 있음.
- list, dict

## primitive type

- C언어에서는 원시 타입의 자료형 (int, long, short ..) 만을 사용.
  - 물리 메모리에 타입 크기 만큼의 공간을 할당되어 효율적임.
  - 객체 처럼 편리하고 다양한 기능을 일일이 구현.
- C에서는 primitive type만을, java에서는 그에 대한 object까지 둘다 제공
- python에서는 primitive type을 제공하지 않음! only 객체.

## Object

- 파이썬은 모든 것이 객체로 표현되며, `mutable object`와 `immutable object`로 나뉨.
  - `mutable` : list, dict, set
  - `immutable` : bool, int, float, tuple, str

### immutable 객체

- 메모리 영역에 할당되면, 값을 수정할 수 없음.
- str, int, **tuple** 등등
- tuple은 read-only 용도의 list로 사용할 수 있고, dict의 key나 set의 value로 사용될 수 있음. (list는 안됨)

### mutable 객체

- see [object.ipynb](object.ipynb)

### `is` vs `==`

- `is` : 변수가 가리키는 Object의 id를 비교하는 연산자
  ```python
    if a is None :  # None은 value가 없어서 == 을 쓰면 안됨.
        pass
  ```
- `==` : 값 자체를 비교하는 연산자
  ```python
    if a ==
  ```
