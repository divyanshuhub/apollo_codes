#User function Template for python3


# Structure of the node of the tree is as

'''class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None'''




# function should return the count of total number of non leaf nodes in the tree
class Solution:
    def countNonLeafNodes(self, root):
        # add code here
        def tra(root):
            x = 0
            if root:
                if not root.left and not root.right:
                    pass
                else:
                    x+=1 + tra(root.left) + tra(root.right)
            return x
            
        
        return tra(root)
        
