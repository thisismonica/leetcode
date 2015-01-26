DEBUG = True
def log(s):
    if DEBUG:
        print s

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

     def __str__(self, depth=0):
        res = ""
        
        # Print right branch
        if self.right != None:
            res += self.right.__str__(depth+1)

        # Print self
        res += "\n" +("    "*depth) +str(self.val)

        # Print left branch
        if self.left != None:
            res += self.left.__str__(depth+1)

        return res
'''
Given a binary tree where all the right nodes are either leaf nodes with a sibling or empty.
Flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
'''
class Solution:
    def answer(self, root):

        # Nodes to record parent and parent's right node
        parent, parent_right = None, None
        node = root
        while node is not None:
            # First store curr node and its right for next iteration
            curr_left, curr_right = node.left, node.right
            
            # Pass parent and its right to node
            node.left, node.right = parent_right, parent

            # Go to next iteration
            parent_right, parent = curr_right, node
            node = curr_left
        return parent

# Testing
s = Solution()
nodes = [TreeNode(i) for i in range(1,6) ]
root  = nodes[0]
root.left, root.right = nodes[1],nodes[2]
nodes[1].left, nodes[1].right = nodes[3], nodes[4]

print "Tesing: \n",root
print "Answers: \n",s.answer(root) 
                
                 
