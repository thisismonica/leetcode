class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if len(ratings)==1:
            return 1
        
        candy = [1 for i in range( len(ratings) ) ]
        c1 = copy.copy(candy)
        c2 = copy.copy(candy)
        for i in range(1, len(ratings) ):
            if ratings[i] > ratings[i-1]:
                c1[i] = c1[i-1] + 1
        for i in reversed(range(0, len(ratings)-1) ):
            if ratings[i] > ratings[i+1]:
                c2[i] = c2[i+1] + 1 
        
        for i in range(len(c1)):
            candy[i] = max( c1[i], c2[i] )
        
        
        return sum(candy)
    