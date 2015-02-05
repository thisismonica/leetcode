class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        res = []
        stack = []
        if root:
            stack.append(root)
        
        while stack != []:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append( curr.right )
            if curr.left:
                stack.append( curr.left )

        return res