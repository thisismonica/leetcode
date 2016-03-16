# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and result and node.right.val != result[-1]:
                    stack.append(node)
                    node = node.right
                else:
                    next = None if node.right and result and node.right.val == result[-1] else node.right
                    result.append(node.val)
                    node = next
        return result
s = Solution

                
        