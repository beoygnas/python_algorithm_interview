# 23. 다이나믹 프로그래밍

문제를 각각의 작은 문제로 나누어 해결한 결과를 저장했다가, 나중에 큰 문제와 결합하여 풀이하는 알고리즘

- Optimal Substructure : 최적부분구조, 문제의 최적 해결 방법이 문제에 대한 최적해결방법을 구성되는 경우에 풀이가 가능하다.
- Overlapping Subproblem : DP의 경우 중복되는 하위 문제들()의 결과를 저장해뒀다가 풀이하며, 중복되지 않는 문제들인 병합정렬, 퀵정렬 등의 분할 정복 알고리즘과는 다르게 분류된다.

### DP, Greedy, 분할정복

| 알고리즘            | 특징                                               | 풀이 가능한 문제 및 알고리즘                           |
| ------------------- | -------------------------------------------------- | ------------------------------------------------------ |
| 다이나믹 프로그래밍 | Optimal Substructure <br> Overlapping Substructure | 0-1 배낭문제 <br>피보나치 수열 <br>다익스트라 알고리즘 |
| 그리디 알고리즘     | Optimal Substructure <br> Greedy Choice Property   | 분할 가능 배낭 문제 <br>다익스트라 알고리즘            |
| 분할정복            | Optimal Substructure                               | 병합정렬 <br> 퀵정렬                                   |

### Optimal Substructure, 최적 부분 구조

- 문제의 최적 해결 방법이 부분 문제에 대한 최적 해결 방법으로 구성되는 경우
- 분할 정복으로 풀 수 있으며, DP 또는 그리디가 적용될 수 있는 후보가 된다.

### Overlapping Subproblem, 중복된 하위 문제들

- 재귀로 풀 때, 반복적으로 동일한 하위문제가 발생하는 경우
- 병합정렬은 이런 중복 문제가 발생하지 않아 DP로 해결할 수 없다!

### DP 방법론

- 상향식 (Bottom-up, tabulation)
- 하향식 (Top-down, memoization)

### 0-1 배낭문제

모든 경우의 수를 계산해야 할때, 중복된 하위문제를 이용하여 그 순간순간의 최적의 값만을 기록한다.

## 문제

85. 피보나치 수 : https://leetcode.com/problems/fibonacci-number
86. 최대서브배열 : https://leetcode.com/problems/maximum-subarray
87. 계단 오르기 : https://leetcode.com/problems/climbing-stairs
88. 집 도둑 : https://leetcode.com/problems/house-robber
