# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    # Create tree from input array.
    #
    # Example input, [3,2,3,null,3,null,1], generate Tree:
    #     3
    #    / \
    #   2   3
    #    \   \
    #     3   1
    #
    # Return the root node 3
    def __init__(self, array):
        self.root = TreeNode(array[0])

        nodeMap = [None for i in range(len(array))]
        nodeMap[0] = self.root

        for i in range(len(array)):
            node = nodeMap[i]
            if node:
                leftChild = 2*i + 1
                rightChild = leftChild + 1
                if leftChild < len(array):
                    node.left = TreeNode(array[leftChild])
                    nodeMap[leftChild] = node.left

                if rightChild < len(array):
                    node.right = TreeNode(array[rightChild])
                    nodeMap[rightChild] = node.right


    def __str__(self):
        return self.display(self.root)

    def display(self, root, depth=0):
        ret = ""

        # Print right branch
        if root.right != None:
            ret += self.display(root.right, depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(root.val)

        # Print left branch
        if root.left != None:
            ret += self.display(root.left, depth + 1)

        return ret



if __name__ == "__main__":

    test = [3,2,3,None,3,None,1]
    print("Creating ")
    root = BinaryTree(test)
    print(root)
