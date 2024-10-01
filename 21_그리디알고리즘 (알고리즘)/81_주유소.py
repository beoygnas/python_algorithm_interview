# https://leetcode.com/problems/gas-station

# 0. 문제의 특수성을 이용.
# 그리디하게 그 순간의 값만 더하고 0아래로 떨어지는 순간은 제외시킨다.
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_sum = 0
        answer = -1
        
        if sum(gas) >= sum(cost):
            for i in range(len(gas)) : 
                if gas_sum + (gas[i] - cost[i]) < 0 : 
                    gas_sum = 0
                elif gas_sum >= 0 :
                    if gas_sum == 0 :
                        answer = i
                    gas_sum += gas[i] - cost[i]
        
        return answer
