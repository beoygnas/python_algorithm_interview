# 20. 슬라이딩 윈도우

- 정식 알고리즘은 아니지만, 투포인터와 함께 자주 사용되는 중요한 기법
- 정렬 여부에 상관없이 많이 사용함
- 투 포인터 vs 슬라이딩 윈도우
  | 이름 | 정렬 여부 | 윈도우 사이즈 | 이동|  
  | ------- | ------- | ------- | ---- |
  | 투 포인터 | 대부분 O | 가변 | 양방향
  | 슬라이딩윈도우 | X | 고정 | 단방향
- 본래는 네트워크 호스트 간 패킷 흐름을 제어하기 위한 방법을 지칭하는 용어
  - 고정 사이즈의 윈도우가 옆으로 이동하면서, 그 다음 패킷들을 전송하는 방식을 말함.

## 문제

75. 최대 슬라이딩 윈도우 : https://leetcode.com/problems/sliding-window-maximum
76. 부분 문자열이 포함된 최소 윈도우 : https://leetcode.com/problems/minimum-window-substring
77. 가장 긴 반복 문자 대체 : https://leetcode.com/problems/longest-repeating-character-replacement
