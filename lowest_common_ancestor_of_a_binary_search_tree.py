# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        left, right = min(p.val,q.val), max(p.val,q.val)
        node = root
        while node:
            if node.val>right:
                node=node.left
            elif node.val<left:
                node=node.right
            else:
                break
        return node


