# 16. 트라이

- 트라이(Trie)는 검색 트리의 일종으로, 일반적으로 키가 문자열인, 동작 배열 또는 연관 배열을 저장하는데 사용되는 정렬된 트리 자료구조이다.
- 문자열 탐색을 위한 자료구조로 널리쓰이고, `retrieval`에서 따왔다.
- 트리와 유사하지만, binary 트리 보단, m-ary Tree의 형태를 주로 띈다.
- 문자열을 위한 트리의 형태이기 때문에, 사실상 문자 개수만큼 자식이 있다.

## 문제

56. 트라이 구현 : https://leetcode.com/problems/implement-trie-prefix-tree
57. 팰린드롬 페어 : https://leetcode.com/problems/palindrome-pairs

## 기록

### 1. staticmethod 데코레이터

- `@stacticmethod` 데코레이터가 붙은 method는, 클래스와 독립적은 함수로서의 의미가 강하게 갖는다. [57\_팰린드롬페어.py](57_팰린드롬페어.py) 에서도, `is_palindrome()`과 같은 고유한 의미를 갖는 함수를 클래스 내에 선언할 경우에 데코레이터를 붙였다.

```python
class CLASS :
    def a(self) :
        pass

    @stacticmethod
    def b() :
        pass
```
