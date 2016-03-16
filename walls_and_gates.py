class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms == []:
            return
        queue = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        while queue:
            i, j = queue.pop(0)
            
            if i-1 >= 0 and rooms[i-1][j] != -1 and rooms[i-1][j] > rooms[i][j]+1:
                rooms[i-1][j] = rooms[i][j]+1
                queue.append((i-1, j))
            if i+1 < len(rooms) and rooms[i+1][j] != -1 and rooms[i+1][j] > rooms[i][j]+1:
                rooms[i+1][j] = rooms[i][j]+1
                queue.append((i+1, j))
            if j-1 >= 0 and rooms[i][j-1] != -1 and rooms[i][j-1] > rooms[i][j]+1:
                rooms[i][j-1] = rooms[i][j]+1
                queue.append((i, j-1))
            if j+1 < len(rooms[0]) and rooms[i][j+1] != -1 and rooms[i][j+1] > rooms[i][j]+1:
                rooms[i][j+1] = rooms[i][j]+1
                queue.append((i, j+1))