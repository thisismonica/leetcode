class Solution:
    def peek(self, stack):
        if stack==[]:
            return None
        else:
            return stack[-1]
            
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        node = root
        stack = []
        res = []
        end = False
        
        while not end:
            if node:
                if node.right:
                    stack.append( node.right )
                stack.append(node)
                node = node.left
            else:
                if stack == []:
                    end = True
                else:
                    node = stack.pop()
                    if node.right is not None and node.right==self.peek(stack):
                        temp = node
                        node = stack.pop()
                        stack.append(temp)
                    else:
                        res.append(node.val)
                        node = None
            
        return res            