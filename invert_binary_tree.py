class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is None:
            return None
        
        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)
        right = root.right
        root.right= root.left
        root.left=right
        return root