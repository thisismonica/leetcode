class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        min_price = min(prices[0], prices[1])
        max_profit = prices[1] - prices[0]
        
        for i in range(2, len(prices)):
            min_price = min( min_price, prices[i] )
            max_profit = max( prices[i]-min_price, max_profit)
        
        return max( max_profit,0)