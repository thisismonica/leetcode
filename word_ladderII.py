DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def getSubgraph(self, start, end ,dict):
        # Help function to get neighbors of word
        def neighbors(word, dict):
            neighbors = []
            characters = [ chr( i+ord('a') ) for i in range(26)]
            for i in range( len(word) ):
                for c in characters:
                    if word[i] != c:
                        transform_word = word[:i] + c + word[i+1:]
                        if transform_word in dict:
                            neighbors.append(transform_word)
            return neighbors


        sub_graph = {} # Parents node from end. if end<->n1, then sub_graph[n1] = end
        curr_level = set( [end] )
        prev_level = set()
        reach_start = False

        # BFS level traversal from end to start 
        while not reach_start:
            next_level = set()
            for word in curr_level:
                for n in neighbors( word, dict ):
                    if n not in curr_level and n not in prev_level: # Avoid duplicate, check 2 levels is enough!
                        next_level.add(n)
                        if n == start:
                            reach_start = True
                        if n not in sub_graph: sub_graph[n] = []
                        sub_graph[n].append(word)
            prev_level = curr_level
            curr_level = next_level
            if len( next_level ) == 0:
                 return {}
        return sub_graph

    def findLadders(self, start, end, dict):
        dictionary = {}
        for d in dict:
            dictionary[d] = True

        sub_graph = self.getSubgraph(start,end,dictionary)
        
        # No valid paths found
        if sub_graph == {}:
            return []

        # DFS for each possible shortest path
        self.res = []
        self.dfs([], start, sub_graph)
        return self.res

    def dfs(self, path, curr, sub_graph):
        new_path = path+[curr]
        if curr not in sub_graph:
            self.res.append( new_path )
            return
        for parent in sub_graph[curr]:
            self.dfs(new_path, parent, sub_graph)

# Testing
s = Solution()
test1 = "hot"
test2 = "dog"
test3 = ["hot","dog"]
expect = ["hot", "dog"]
print "Tesing: ",test1, test2, test3
print "Expecting: ",expect
print "Answers: ",s.findLadders(test1, test2, test3) 
