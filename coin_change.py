import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [sys.maxint] * (amount + 1)
        for c in coins:
            if c <= amount:
                dp[c] = 1

        for i in range(1, amount + 1):
            for c in coins:
                if i-c > 0 and dp[i-c] != sys.maxint:
                    dp[i] = min(dp[i], 1 + dp[i-c])

        return dp[-1] if dp[-1] < sys.maxint else -1

    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if(amount == 0):
            return 0

        total = [-1] * amount
        for x in range(amount):
            if x + 1 in coins:
                total[x] = 1
            else:
                all = [total[x-c] for c in coins if x>=c and total[x-c] != -1]
                if(len(all) > 0):
                    total[x] = min(all) + 1

        return total[-1]

s = Solution()
coins = [370,417,408,156,143,434,168,83,177,280,117]
amount = 9935

import time
s1 = time.time()
result1 = s.coinChange(coins, amount)
time1 = time.time() - s1
s2 = time.time()
result2 = s.coinChange2(coins,amount)
time2 = time.time() - s2

print "Result1: ", result1, " Time1: ", time1
print "Result2: ", result2, " Time2: ", time2