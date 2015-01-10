DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    '''
    Given a set of candidates numbers (C) and a target number (T), find all unique combinations in C where the candidates numbers sums to T.
    - All numbers positive
    - Elements in solution set should be non-descending
    - Repeated number from C is NOT allowed
    C=[2,3,6,7], target = 7
    Answer = [2,2,3]
    '''
    # Define dfs function for recursion
    # Assume candidates sorted and all less equal to target
    def dfs( self, candidates, target, prev):
        if target == 0:
            self.res.append( prev )

        if candidates == []:
            return

        # Iterate reversely to enumerate each combination
        for i in range(len(candidates)): 

            # Skip same value candidate to avoid duplicate
            if i>0 and candidates[i]==candidates[i-1]:
                continue

            # Return if current element > target
            if candidates[i] > target:
                return

            remaining = target - candidates[i]
            self.dfs( candidates[i+1:], remaining, prev+[candidates[i]] )
        return 

    def combinationSum(self, candidates, target):
       
        # Sort candidate list
        candidates.sort()
        self.res = []

        # DFS on the candidates
        self.dfs(candidates, target, [] )
        return self.res


# Testing
s = Solution()
test1 = [10,1,2,7,6,1,5]
test2 = 8
print "Tesing: ",test1, test2
print "Answers: ",s.combinationSum(test1, test2) 
                
                 
