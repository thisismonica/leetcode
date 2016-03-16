# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if root is None:
            return []
        queue = [(root,1)]
        rightSide = []
        i = 0
        while queue:
            node, layer = queue.pop(0)
            if layer==i+1:
                rightSide.append( node.val )
                i += 1
            if node.right:
                queue.append( (node.right,layer+1) )
            if node.left:
                queue.append( (node.left, layer+1) )
        return rightSide
