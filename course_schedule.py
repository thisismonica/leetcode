class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        graph = [ [] for i in range(numCourses) ]
        color = [ 0 for i in range(numCourses) ]
        for p in prerequisites:
            if p[1] not in graph[p[0]]:
                graph[p[0]].append( p[1] )
    
        for i in range( numCourses ):
            if self.dfsCycle(i,graph,color):
                return False
return True
    
    def dfsCycle(self,i,graph,color):
        if color[i]==2:
            return False
        color[i] = 1
        for c in graph[i]:
            if color[c] == 1 or self.dfsCycle(c,graph,color):
                return True
        color[i] = 2
        return False
