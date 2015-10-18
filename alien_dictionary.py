class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.graph = {}
        self.buildGraph(words)
        print "Graph: ",self.graph
        
        self.visited = {}
        for n in self.graph:
            self.visited[n] = 0
            
        self.stack = []
        self.hasCircle = False
        for n in self.graph:
            if self.visited[n] == 0:
                self.dfs(n)
            if self.hasCircle:
                return ""
               
        return "".join(reversed(self.stack))
    
    def buildGraph(self, words):
        for w in words:
            for l in w:
                if l not in self.graph:
                    self.graph[l] = set()
        
        for i in range(1, len(words)):
            k = 0
            while k < min(len(words[i]), len(words[i-1])) and words[i][k] == words[i-1][k]:
                k += 1
            if k < min(len(words[i]), len(words[i-1])):
                self.graph[words[i-1][k]].add( words[i][k] )
        
    def dfs(self, n):
        self.visited[n] = 1
        print "dfs: letter = ",n
        
        for c in self.graph[n]:
            if self.visited[c] == 0:
                self.dfs(c)
            if self.visited[c] == 1:
                self.hasCircle = True
                return
        self.visited[n] = 2
        
        self.stack.append(n)
s = Solution()
words = ["ze","yf","xd","wd","vd","ua","tt","sz","rd", "qd","pz","op","nw","mt","ln","ko","jm","il", "ho","gk","fa","ed","dg","ct","bb","ba"]
print s.alienOrder(words);
        
        