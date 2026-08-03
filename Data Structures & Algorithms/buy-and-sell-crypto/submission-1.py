class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for price in prices:
            buy_price = min(price, buy_price)
            profit = max(price - buy_price, profit)
        
        return profit
                
