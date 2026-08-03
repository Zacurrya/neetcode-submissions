class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l,r = 0,1
        while l < r and r < len(prices):
            diff = prices[r] - prices[l]
            res = max(res, diff)
            
            if prices[l] > prices[r]:
                l = r
            r += 1
        
        return res
                
