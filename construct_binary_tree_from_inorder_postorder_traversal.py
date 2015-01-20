# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        root = "\nroot="+ str(self.val)
        if self.left:
            l = "\tleft="+ "("+str(self.left.val) +")"
        else:
            l = "\tleft=None"
        if self.right:
            r = "\tright="+ "("+str(self.right.val) +")"
        else:
            r = "\tright=None"
        return root+l+r
        
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        
        # Define subTree function to call recursively
        def subTree(inorder, postorder, start_in, start_post, length):
            if length <= 0:
                return None
            if length == 1:
                return TreeNode( inorder[start_in] )
                
            if inorder[start_in:start_in+length] == postorder[start_post:start_post+length]:
                r = TreeNode(0)
                node = r
                for num in reversed( inorder ):
                    node.left = TreeNode( num )
                    node = node.left
                return r.left
                
            # Find the length of left subtree by target root
            root_val = postorder[ start_post + length-1 ]
            root_node = TreeNode( root_val )
            root_index = inorder.index( root_val )
            left_len = root_index - start_in
            right_len = length - left_len - 1
            
            # Construct binary tree recursively
            root_node.left = subTree( inorder, postorder, start_in, start_post, left_len)
            root_node.right = subTree( inorder, postorder, start_in+left_len+1, start_post+left_len, right_len)
            
            return root_node
            
        if len(inorder) != len(postorder):
            return None
            
        length = len(inorder)
        return subTree(inorder, postorder, 0, 0, length )

s = Solution()
test1 = [1,2,5]
test2 = [1,2,5]
#print "Answer of :",test1, test2
print s.buildTree(test1, test2)       