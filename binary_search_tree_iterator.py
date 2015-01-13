class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self._stack = []
        self._root = root
        node = self._root
        if node is not None:
            self._stack = [node]
            while node.left is not None:
                node = node.left
                self._stack.append( node )
            
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self._stack != []

    # @return an integer, the next smallest number
    def next(self):
        if self._stack != []:
            node = self._stack.pop()
            res = node.val
            if node.right is not None:
                node = node.right
                self._stack.append( node )
                while node.left is not None:
                    node = node.left
                    self._stack.append( node )
            return res
                

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())