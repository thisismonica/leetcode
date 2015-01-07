DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def maxProfit(self, prices):
        N = len(prices)
        if N <=1:
            return 0
        # Max profit of 1 transaction, starting from 0 to i
        dp_left = [0 for i in range(N)]
        dp_left[0] = 0
        min_price = prices[0]
        for i in range(1,N):
            min_price = min(prices[i], min_price)
            dp_left[i] = max( dp_left[i-1], prices[i]-min_price )
        
        log(dp_left)

        # Max profit of 1 transaction, starting from i to len(prices)-1
        dp_right = [0 for i in range(N)]
        dp_right[N-1] = 0
        max_price = prices[N-1]
        for i in reversed( range(N-1) ):
            max_price = max(prices[i], max_price)
            dp_right[i] = max( dp_right[i+1],max_price-prices[i])

        log(dp_right)

        # Max profit of 2 transaction
        max_profit = 0
        for i in range( N ):
            max_profit = max(max_profit, dp_left[i]+dp_right[i])
        return max_profit
# Testing
s = Solution()
test = [2,1,2,0,1]
print "Tesing: ",test
print "Answers: ",s.maxProfit(test) 
                
                 
