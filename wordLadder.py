import copy
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        # BFS for shortest path
        q = [start]
        wordLen = len(start)
        g = {start:[]}
        visited = set()
 
        while q:
            word = q.pop(0)
	    visited.add(word)

            if word not in g: g[word] = []

            # Find neighbor
	    i, found = 0, False
            while i < wordLen and not found:
                left, right = word[:i], word[i+1:]
                for r in "abcdefghijklmnopqrstuvwxyz":
		    if r != word[i]:
			    newWord = left+r+right
			    if newWord == end:
				g[word].append( newWord )
				found = True
				if newWord in dict:
					dict.remove( newWord )
				break
			    elif newWord in dict and newWord not in visited:
				dict.remove(newWord)
				g[word].append( newWord )
				q.append( newWord )
	    	i = i+1
        # DFS to get path
        self.paths = []
	print "graph: ",g
        self.dfs(g, start, end, [])
        minLen = min( [ len(p) for p in self.paths ])
        res = []
        for p in self.paths:
            if len(p) == minLen:
                res.append(p)
	print "minLen: ",minLen," res: ",res
        return res
        
    def dfs(self, g, start, target, path):
        if start is None:
            return
	print "[dfs] path: ",path," target: ",target," self.path: ",self.paths
        path.append(start)
        if start == target:
            self.paths.append( path )
            return

        for n in g[start]:
	    oldPath = copy.copy(path)
            self.dfs(g, n, target, oldPath )
        return

s = Solution()
start = "hot"
end = "dog"
dict = ["hot","dog"]
#print " solution is: "
#print s.findLadders(start,end,dict)
s.findLadders(start,end,dict)
