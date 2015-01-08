# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.gen(1,n)
    
    def gen(self, start, end):
        if start > end: return [None]
        if start == end:
            return [TreeNode(start)]
        res = []
        for i in range( start, end+1 ):
            left = self.gen(start,i-1)
            right = self.gen(i+1, end)
            for l in left:
                for r in right:
                    t = TreeNode(i)
                    t.left = l
                    t.right = r
                    res.append(t)
        return res
        '''
            1                 2                    n
            \              /   \                 /
            (2~n),      (1)   (3,n), ...,    (1,n-1)
            '''


















