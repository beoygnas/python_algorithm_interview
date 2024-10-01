# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

# 0. 일단 사고 최대일때까지 뻐팅긴다.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        recent_price = prices[0]
        profit = 0

        for i in range(1, len(prices)) : 
            if prices[i] < recent_price : 
                profit += recent_price - prices[buy_day]
                buy_day = i
        
            recent_price = prices[i]
                
        profit += recent_price - prices[buy_day]
        return profit


# 1. 리팩토링
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1) : 
            if prices[i+1] > prices[i] :
                profit += prices[i+1] - prices[i]
        return profit
    
# 2 파이썬 버젼
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))