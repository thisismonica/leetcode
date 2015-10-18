# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        stack = []
        order = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                order.append(node.val)
                node = node.right
                
        i = 0
        while i < len(order) and order[i] < target:
            i += 1
        j = i-1
        res = []
        while len(res) < k and i < len(order) and j >= 0:
            if target - order[j] < order[i] - target:
                res.append(order[j])
                j -= 1
            else:
                res.append(order[i])
                i += 1
        if len(res) < k:
            if i == len(order):
                res.extend(order[j - (k - len(res)) + 1:j+1][::-1])
            else:
                res.extend(order[i:i + (k - len(res))])
        return res
            
                