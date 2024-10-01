# 21. 그리디 알고리즘

그리디 알고리즘은 global optima를 찾기 위해, 각 단계에서 local 최적의 선택을 하는 휴리스틱 문제 해결 알고리즘이다.

- 대부분은 optimum이 아니지만, 드물게 최적해를 보장하는 경우가 있다.
- 그리디 알고리즘이 작동하는 문제들은 Greedy Choice Property를 갖고 있는 Optimal Substructure인 문제들.
- 다익스트라 알고리즘, 허프만 코딩 알고리즘 등이 최적해를 보장함.

### DP vs Greedy

- 최적 부분 구조(Optimal Substructure) 문제를 푼다는 점에서 DP와 비슷하지만, 성격이 다르고 접근 방식 또한 다르다.
- DP : 하위 문제에 대한 최적의 솔루션을 찾고, 이 결과들을 결합한 정보에 입각해 global optimum solution을 찾는다.
- Greedy : 각 단계마다 로컬 최적해를 찾는 문제로 접근하여, 문제를 더 작게 줄여나가는 형태로 DP와 반대 반향으로 접근하게 됨.

### 배낭문제

- Fractional Knapsack Problem : Greedy
- Non-Fractional Knapsack Problem : DP

### 동전 바꾸기 문제

- 동전이 모두 배수의 관계이면, 그리디 알고리즘으로 동전의 개수를 최소로 할 수 있다.
- 배수 관계가 아니라면, dynamic programming으로

## 문제

78. 주식을 사고팔기 가장 좋은 시점2 : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
79. 키에 따른 대기열 재구성 : https://leetcode.com/problems/queue-reconstruction-by-height
80. 태스크 스케쥴러 : https://leetcode.com/problems/task-scheduler
81. 주유소 : https://leetcode.com/problems/gas-station
82. 쿠키부여 : https://leetcode.com/problems/assign-cookies

## 기록
