class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        s = 0
        start = 0
        
        for i, g in enumerate(gas):
            s = s + g-cost[i]
            if s < 0:
                s = 0
                start = i+1
                
        if s>=0:
            return start
                
        return -1