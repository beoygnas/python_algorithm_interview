# https://leetcode.com/problems/sliding-window-maximum

# 0. 시간초과
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 시간 복잡도 O(nk)
        # O(n log k)
        # 슬라이딩 윈도우를 힙으로 유지하면 될듯, 빠진게 최대값일 경우에 heappop
        answer = []
        window = collections.deque()
        max_value = float('-inf')

        for i, v in enumerate(nums): 
            window.append(v)
            if i < k-1 :
                continue

            if max_value == float('-inf'):
                max_value = max(window)
            elif v > max_value :
                max_value = v
            
            answer.append(max_value)

            if max_value == window.popleft() : 
                max_value = float('-inf')
        
        return answer