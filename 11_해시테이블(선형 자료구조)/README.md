# 11. 해시테이블

- hash table 또는 hash map은 키를 key를 value에 mapping할 수 있는 구조인, 연관 배열 ADT를 표현하는 자료구조이다.
- 대부분의 연산이 `O(1)`로, 데이터 양에 관계없이 빠른 성능을 기대할 수 있다.

### Hash

- `hash function` : 임의 크게 데이터를 고정 크기 값으로 매핑하는데 사용할 수 있는 함수
- `hashing` : hash table에 indexing 하기 위해 hash function를 사용하는 것.
- 최적의 검색이 필요한 분야 (DB), checksum, 손실압축, 암호 등 여러 분야에서 사용
- 성능 좋은 hashing은 다음을 포함한다.
  - collision 최소화
  - 쉽고 빠른 연산 (시간복잡도가 낮은 hash function)
  - hash table 전체에 해시 값이 고르게 분포.
  - 사용할 키의 모든 정보를 이용하여 해싱
  - hash table 사용 효율이 높을 것.

### Load Factor

- 해시테이블에 저장된 데이터 개수를 n을 버킷의 개수 m으로 나눈 것 (`n/m`)
- hash function이 key를 잘 분산해 주는 지에 대한 효율성에 대한 지표.
  - java에서는 `0.75`가 default load factor (데이터가 3개면, key는 4개이도록 hashing)

### Hash fucntion

- hashing algorithm은 다양하지만, 그 중 대표적인 정수형 해싱 기법인 `Modulo-Division Method` 가 있다.
- `h(x) = x mod m`, m은 해시 테이블의 크기, x는 간단한 규칙을 통해 만들어낸 충분히 랜던함 상태의 key의 값
  - key가 index가 되기 위해, key가 문자열이라면 어떤 값이 되어야함.
  - ex) java에서는 key x 에 대하여, 그 값을 다음 다항식의 결과로 제시
    - `P(x) = s[0] + x^(n-1) + s[1] + x^(n-2) ...`

### Collision

- hash function이 아무리 좋아도, collision은 발생할 수 있다. 이를 막기 위한 방법들
- `chaning`
  - index(hash function의 결과)에 이미 값이 있다면, linked list로 연결
  - pros : 간단한 구현, 대체적으로 `O(1)`에 탐색이 가능
  - cons : 최악의 경우 `O(n)`
- `open addressing`
  - collision 발생 시, `probing`을 통해 아직 value가 없는 open address를 찾는 방식
  - pros (Linear Probing) : 구현방법이 간단, 전체적인 성능이 나쁘지 않음.
  - cons : chaining에 비해 저장용량에 제한이 있으며, 모든 원소가 자신의 해시값과 일치하는 주소에 저장된다는 보장이 없다.
    - `Clusterring` : collision이 많이 발생하여, 여기저기에 연속된 데이터 그룹이 발생. 클러스터끼리 합쳐지게 되면, 데이터가 몰리게 되고, probing이 더 오래 걸리게 됨.
  - 데이터가 버킷사이즈보다 많은 경우에는, 더이상 삽입이 안됨. (이미 다 찼기 때문) 버킷 사이즈보다 커지거나, load factor 비율을 넘어서면 더 큰 크기의 버킷을 생성하고, 새롭게 복사하는 `rehashing` 작업이 발생. (`list`의 doubling 방식의 동적할당과 비슷)

### Python Dict

- 해시테이블로 구현된 파이썬 자료형
- `Open Addressing` 방식을 채용. (chaning은 매번 malloc으로 메모리를 할당하는 오버헤드가 높아 open addressing을 선택)

## 문제

28. 해시맵 디자인 : https://leetcode.com/problems/design-hashmap
29. 보석과 돌 : https://leetcode.com/problems/jewels-and-stones

## 기록

### 1. `key in dict` 의 시간복잡도는 O(1)

- hash table에서 key가 있는지 체크하는 것은, 다음 과정을 거침
  - key를 hashing, hash value를 get
  - hash value로 배열에 접근
  - 배열에 저장된 (key, value) pair (또는 item)이 key와 같은지를 check
  - 이는 상수시간 내에 이루어진다.
