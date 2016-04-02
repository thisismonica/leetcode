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
                    if array[leftChild]:
                        node.left = TreeNode(array[leftChild])
                    else:
                        node.left = None
                    nodeMap[leftChild] = node.left

                if rightChild < len(array):
                    if array[rightChild]:
                        node.right = TreeNode(array[rightChild])
                    else:
                        node.right = None
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

    def btree2Array(self, root):
        def dfs(node, depth):
            if node is None:
                self.depth = max(self.depth, depth)
                return

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        self.depth =  0
        dfs(root, 0)

        array = []
        queue = [(root, 0)]
        while queue:
            node, layer = queue.pop(0)
            if node:
                array.append(node.val)
            else:
                array.append(0)

            # Don't push node in last layer
            if layer != self.depth - 1:
                if node:
                    queue.append((node.left, layer+1))
                    queue.append((node.right, layer+1))
                else:
                    queue.append((None, layer+1))
                    queue.append((None, layer+1))
        return array



if __name__ == "__main__":

    test = [3,2,3,None,3,None,1]
    print("Creating ")
    root = BinaryTree(test)
    print(root)
