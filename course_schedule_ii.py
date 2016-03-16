class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        graph = [ [] for i in range(numCourses) ]
        color = [0]*numCourses
        self.order = []
        
        for p in prerequisites:
            if p[1] not in graph[ p[0] ]:
                graph[ p[0] ].append( p[1] )
    
        for i in range(numCourses):
            if color[i] != 2:
                if self.dfs(i, graph, color):
                    return []
return self.order
    
    def dfs(self, i ,graph, color):
        if color[i] == 2:
            return False
        color[i] = 1
        for j in graph[i]:
            if color[j] == 1 or self.dfs(j,graph,color):
                return True
        color[i] = 2
        self.order.append(i)
        return False