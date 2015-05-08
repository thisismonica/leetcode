DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self,k,prices):
        def maxProfitManyTransactions(prices):
            profit = 0
            for i in range(1,len(prices)):
                diff = prices[i] - prices[i-1]
                if diff > 0:
                    profit += diff
            return profit
        
        # If k >= len(prices)/2, same as Best Time To Buy And Sell Stock II
        if k >= len(prices)/2:
            return maxProfitManyTransactions(prices)
        
        #Array of max profit for each day with current day sell
        today_sell_max = [0] * (k+1)
        
        # Array of max profit for each day with previous day sell
        prev_sell_max = [0] * (k+1)
        
        for i in range(1,len(prices) ):
            diff = prices[i] - prices[i-1]
            
            for j in reversed(range(1,k+1)):
                today_sell_max[j] = max(today_sell_max[j]+diff, prev_sell_max[j-1]+max(diff,0) )
                prev_sell_max[j] = max( prev_sell_max[j], today_sell_max[j] )
                
        return prev_sell_max[k]

# Testing
s = Solution()
test1 = [3,2,6,5,0,3]
test2 = 2
print "Tesing: ",test1,test2
print "Answers: ",s.answer(test2,test1)
