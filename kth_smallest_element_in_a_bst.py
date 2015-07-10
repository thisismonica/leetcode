class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        ith = 0
        node = root
        stack = []
        
        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack!=[]:
                node = stack.pop()
                ith += 1
                if ith == k:
                    return node.val
                node = node.right
            else:
                return
