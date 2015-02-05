class Solution:
    # @param points, a list of Points
    # @return an integer
    
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)
        res = 0
        
        for i in range( len(points) ):
            k = {'inf':0} # 'inf' stands for vertical line
            dup = 0
            
            # Check the rest of points for same slope        
            for j in range( len(points) ):
                
                # Count duplicates
                if points[i].x==points[j].x and points[i].y==points[j].y: 
                    dup = dup + 1
                    continue
                
                # Calculate slope
                if points[i].x == points[j].x:
                    slope = 'inf'
                else:
                    slope =  1.0*(points[i].y - points[j].y)/(points[i].x-points[j].x)
                
                # Count number of points with same slope
                k[slope] = k[slope]+1 if slope in k else 1
                
            # Update max
            res = max(res, max(k.values())+dup)
        return res