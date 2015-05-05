class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None: return None
        #BFS
        queue = [(root, 0)]
        prev, prevLayer = None, 0
        while queue:
            curr, layer = queue.pop(0)
            if prev and layer==prevLayer:
                prev.next = curr
            elif prev and layer>prevLayer:
                prev.next = None
            prev, prevLayer = curr, layer
            if curr.left:
                queue.append( (curr.left, layer+1) )
            if curr.right:
                queue.append( (curr.right, layer+1) )