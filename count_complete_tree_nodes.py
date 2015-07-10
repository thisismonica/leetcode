class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root is None:
            return 0
        
        left_count = 0
        node = root
        while node:
            left_count += 1
            node = node.left
        
        right_count = 0
        node = root
        while node:
            right_count += 1
            node = node.right
        
        if right_count == left_count:
            return 2**(right_count) -1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
