class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def bfs(n, i, graph):
            queue = [(i, 1)]
            visited = [False for k in range(n)]

            while queue:
                node,layer = queue.pop(0)
                visited[node] = True

                for a in graph[node]:
                    if not visited[a]:
                        queue.append((a, layer + 1))
            return layer

        def getLeaves(graph, exist_leaves):
            if len(exist_leaves) == len(graph) - 1:
                for i in range(len(graph)):
                    if i not in exist_leaves:
                        return [i]

            leaves = []
            for i in range(len(graph)):
                if len(graph[i]) == 1:
                    leaves.append(i)
            return leaves

        if n <= 2:
            return range(n)

        graph = [set() for i in range(n)]
        for e in edges:
            i,j = e
            graph[i].add(j)
            graph[j].add(i)

        numOfLeaves = 0
        addLeaves = []
        leaves = []
        while numOfLeaves != len(graph):
            for i in addLeaves:
                j = graph[i].pop()
                graph[j].remove(i)

            addLeaves = getLeaves(graph, leaves)
            leaves.extend(addLeaves)
            numOfLeaves += len(addLeaves)

        return addLeaves

n = 4
edges = [[1,0],[1,2],[1,3]]
s = Solution()
print s.findMinHeightTrees(n, edges)