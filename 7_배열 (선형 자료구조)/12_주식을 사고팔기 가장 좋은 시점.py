# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

from typing import * 

# 0,1
# 그날 그날의 최대이익과 최저점을 기록. (일종의 그리디)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
    
        for price in prices[1:] :
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)

        return max_profit