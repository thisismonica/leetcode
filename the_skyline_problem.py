class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        if buildings == []:
            return []
        n = len(buildings)
        if n == 1:
            return self.getSingleSkyline( buildings[0] )
        if n == 2:
            return self.mergeSkyline( self.getSingleSkyline(buildings[0]), self.getSingleSkyline(buildings[1]) )
        res = self.mergeSkyline( self.getSkyline(buildings[:n/2]), self.getSkyline(buildings[n/2:]) )
        return self.removeDuplicate(res)
    
    def getSingleSkyline(self, b):
        return [ [b[0],b[2]], [b[1],0] ]
    
    def mergeSkyline(self, p1, p2):
        if p1 == []:
            return p2
        if p2 == []:
            return p1
        p = []
        i1, i2 = 0, 0
        h1, h2 = 0, 0
        while i1 < len(p1) and i2 < len(p2):
            if p1[i1][0] < p2[i2][0]:
                h1 = p1[i1][1]
                h = max(h1,h2)
                p.append( [p1[i1][0],h] )
                i1 +=1
            else:
                h2 = p2[i2][1]
                h = max(h1,h2)
                p.append( [p2[i2][0], h] )
                i2 += 1
        while i1 < len(p1):
            p.append( p1[i1] )
            i1+=1
        while i2 < len(p2):
            p.append( p2[i2] )
            i2+=1
        return p

    def removeDuplicate(self, p):
        i = 0
        m = []
        while i < len(p):
            m.append(p[i])
            j = i+1
            while j<len(p) and p[j][1]==p[i][1]:
                j+=1
            i = j

        i = 0
        merge = []
        while i < len(m):
            j = i+1
            while j<len(m) and m[j][0]==m[i][0]:
                j+=1
            merge.append(m[j-1])
            i = j
        return merge

s = Solution()
test = [[1,2,1],[1,2,2],[1,2,3]]
print s.getSkyline(test)


