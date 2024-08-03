# 8. 연결리스트

- 연결리스트는 데이터 요소의 선형 집합으로, 데이터의 순서가 메모리에 물리적인 순서대로 저장되지 않는다.
- 동적으로 새로운 노드의 삽입과 삭제가 편하며, 데이터를 구조체로 묶어 포인터로 연결한다는 개념은 다양하게 활용이 가능함.

### 연산별 시간복잡도

| 연산                   | 시간복잡도 | array 시간복잡도 |
| ---------------------- | ---------- | ---------------- |
| `탐색`                 | `O(n)`     | `O(n)`           |
| `head, tail 추가/삭제` | `O(1)`     | `O(n)` / `O(1)`  |

## 문제

13. 팰린드롬 연결 리스트 : https://leetcode.com/problems/palindrome-linked-list/
14. 두 정렬 리스트의 병합 : https://leetcode.com/problems/merge-two-sorted-lists/
15. 역순 연결 리스트 : https://leetcode.com/problems/reverse-linked-list/
16. 두 수의 덧셈 : https://leetcode.com/problems/add-two-numbers/
17. 페어의 노드 스왑 : https://leetcode.com/problems/swap-nodes-in-pairs

## 기록

### 1. deque를 이용한 popleft()

```python
deq = collections.deque()
deq.popleft() # O(1)
deq.pop() # O(1)
```

### 2. runner

- See [13.팰린드롬연결리스트.py](./13_팰린드롬연결리스트.py)
- 연결리스트에서 두 개의 포인터를 이용하는 방법.
  - fast runner : 두칸씩 포인터 이동
  - slow runner : 한칸씩 포인터 이동

### 3. 다중할당

- See [다중할당.ipynb](./다중할당.ipynb)
- python의 다중할당은 트랜잭션으로 처리를 하기 때문에, 같은 객체를 참조하지 않아야 할 때 사용하면 좋다.
- swap 역시, 보통 다중 함수로 처리함.

```python
# 3가지 변수 모두, 서로 다른 객체를 가리키게 됨.
rev, rev.next, slow = slow, rev, slow.next

# rev와 slow가 같은 객체를 참조하게 되어, 두 번째 라인에서 rev의 기댓값이 영향을 받음.
rev, rev.next = slow, rev
slow = slow.next

l1, l2 = l2, l1 # l1과 l2로 swap
```

### 4. Optional[X]

- 자료형 X 아니면 None이라는 뜻으로, kotlin의 ?랑 비슷.

```bash
# list1으로 ListNode 또는 None이 올 수 있다는 뜻으로, 리스트가 아님!
def mergeTwoLists(self, list1: Optional[ListNode]) :

```
